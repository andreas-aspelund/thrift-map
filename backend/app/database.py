import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]


def get_connection():
    """Return a new psycopg2 connection. Caller is responsible for closing it."""
    return psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
