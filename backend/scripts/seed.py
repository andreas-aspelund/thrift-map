"""
Seed script — loads all shops from oslo-shops-seed.json into the database.

Run from the backend/ directory:
    python -m scripts.seed

Requires DATABASE_URL in backend/.env (or already in your environment).
"""

import json
import os
import sys
from pathlib import Path

import psycopg2
from dotenv import load_dotenv

# Load .env from the backend directory (one level up from scripts/)
load_dotenv(Path(__file__).parent.parent / ".env")

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    print("ERROR: DATABASE_URL is not set. Copy backend/.env.example to backend/.env and fill it in.")
    sys.exit(1)

seed_file = Path(__file__).parent / "oslo-shops-seed.json"
with open(seed_file, encoding="utf-8") as f:
    shops = json.load(f)

conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

inserted = 0
skipped = 0

for shop in shops:
    cur.execute(
        """
        INSERT INTO shops (name, address, lat, lng, neighborhood, notes)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (name, address) DO NOTHING
        """,
        (
            shop["name"],
            shop["address"],
            shop["lat"],
            shop["lng"],
            shop.get("neighborhood"),
            shop.get("notes"),
        ),
    )
    if cur.rowcount == 1:
        inserted += 1
    else:
        skipped += 1

conn.commit()
cur.close()
conn.close()

print(f"Done. {inserted} shops inserted, {skipped} already existed (skipped).")
