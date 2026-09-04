-- Enable PostGIS extension (already enabled on Supabase, but safe to repeat)
CREATE EXTENSION IF NOT EXISTS postgis;

-- Shops table
CREATE TABLE IF NOT EXISTS shops (
    id          SERIAL PRIMARY KEY,
    name        TEXT NOT NULL,
    address     TEXT NOT NULL,
    lat         DOUBLE PRECISION NOT NULL,
    lng         DOUBLE PRECISION NOT NULL,
    neighborhood TEXT,
    notes       TEXT,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT shops_name_address_unique UNIQUE (name, address)
);

-- Spatial index for geo queries (distance search etc.) — not needed for MVP
-- but costs nothing to have and unlocks Phase 6 filtering for free.
CREATE INDEX IF NOT EXISTS shops_location_idx
    ON shops
    USING GIST (ST_MakePoint(lng, lat)::geography);
