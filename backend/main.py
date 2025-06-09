from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import create_tables, get_db
from init_data import init_database
from routes import auth, modules, legacy

# FastAPI app
app = FastAPI(
    title="Alquimia del Cambio",
    version="1.0.0",
    description="Aplicación de transformación personal y desarrollo emocional"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "http://localhost:5173",
        "https://*.vercel.app",
        "https://*.railway.app",
        "https://your-domain.com"  # Remplace par ton domaine final
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(modules.router)
app.include_router(legacy.router)

@app.on_event("startup")
def startup_event():
    """Initialize database and create tables on startup"""
    create_tables()
    db = next(get_db())
    try:
        init_database(db)
    finally:
        db.close()

@app.get("/")
def root():
    return {
        "message": "Welcome to Alquimia del Cambio API",
        "version": "1.0.0",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    import os
    # Use Railway's standard port 3000 in production, 8000 for local dev
    port = int(os.environ.get("PORT", 3000 if os.environ.get("RAILWAY_ENVIRONMENT") else 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 