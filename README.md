# Thrift Map

A map app for finding secondhand, vintage, and thrift shops — built mobile-first with React + FastAPI + PostGIS.

## Project structure

```
thrift-map/
├── backend/          FastAPI backend (Python)
│   ├── app/          Application code
│   ├── migrations/   SQL migration files
│   └── scripts/      Utility scripts (seed, etc.)
└── frontend/         React frontend (Vite)
    └── src/
        └── components/
```

---

## Setup

### 1. Database (Supabase)

1. Open your Supabase project → **SQL Editor**
2. Paste and run `backend/migrations/001_create_shops.sql`
3. That's it — the `shops` table is ready.

### 2. Backend (FastAPI)

```bash
cd backend

# Install dependencies
pip install -r requirements.txt

# Copy and fill in your Supabase connection string
cp .env.example .env
# Edit .env — add your DATABASE_URL

# Run the development server
uvicorn app.main:app --reload
# → http://localhost:8000
# → http://localhost:8000/docs  (interactive API docs)
```

**Seed the database** (run once after setting up the table):

```bash
cd backend
python -m scripts.seed
```

### 3. Frontend (React)

```bash
cd frontend

# Install dependencies
npm install

# Copy and fill in the backend URL
cp .env.example .env.local
# Edit .env.local — set VITE_API_URL=http://localhost:8000

# Run the development server
npm run dev
# → http://localhost:5173
```

---

## Deployment

| Part     | Platform  | Notes                                      |
|----------|-----------|--------------------------------------------|
| Frontend | Vercel    | Connect GitHub repo, set root dir to `frontend/`, add `VITE_API_URL` env var |
| Backend  | Railway   | Connect GitHub repo, set root dir to `backend/`, add `DATABASE_URL` env var  |
| Database | Supabase  | Already hosted — just run the migration SQL |

---

## API

| Method | Path        | Description          |
|--------|-------------|----------------------|
| GET    | /health     | Health check         |
| GET    | /shops      | List all shops       |
| GET    | /shops/{id} | Get a single shop    |
