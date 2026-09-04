from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import shops

app = FastAPI(
    title="Thrift Map API",
    description="Backend for the secondhand shop map app.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tighten to your Vercel URL in production
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(shops.router)


@app.get("/health")
def health():
    return {"status": "ok"}
