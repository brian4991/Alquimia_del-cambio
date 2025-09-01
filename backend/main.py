import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from database import create_tables, get_db
from init_data import init_database
from routes import auth, modules, legacy

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent
FRONTEND_DIST = PROJECT_ROOT / "frontend" / "dist"

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
        "http://localhost:5174",
        "https://*.vercel.app",
        "https://*.railway.app",
        "https://your-domain.com"  # Remplace par ton domaine final
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (frontend build) - only if the directory exists
if FRONTEND_DIST.exists():
    # Mount assets directory for JS/CSS files
    assets_dir = FRONTEND_DIST / "assets"
    if assets_dir.exists():
        app.mount("/assets", StaticFiles(directory=str(assets_dir)), name="assets")
    
    # Mount other static files at root level
    app.mount("/static", StaticFiles(directory=str(FRONTEND_DIST)), name="static")

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
    # Serve the frontend index.html
    from fastapi.responses import FileResponse
    index_file = FRONTEND_DIST / "index.html"
    if index_file.exists():
        return FileResponse(str(index_file))
    else:
        return {"message": "Frontend not built. Please run 'npm run build' in the frontend directory."}

@app.get("/api")
def api_root():
    return {
        "message": "Welcome to Alquimia del Cambio API",
        "version": "1.0.0",
        "docs": "/docs"
    }

# Serve specific static files at root level
@app.get("/vite.svg")
def get_vite_svg():
    from fastapi.responses import FileResponse
    file_path = FRONTEND_DIST / "vite.svg"
    if file_path.exists():
        return FileResponse(str(file_path))
    raise HTTPException(status_code=404, detail="File not found")

@app.get("/café.jpg")
def get_cafe_jpg():
    from fastapi.responses import FileResponse
    file_path = FRONTEND_DIST / "café.jpg"
    if file_path.exists():
        return FileResponse(str(file_path))
    raise HTTPException(status_code=404, detail="File not found")



# Catch-all route for React Router (SPA)
@app.get("/{path:path}")
def catch_all(path: str):
    from fastapi.responses import FileResponse
    
    # First, check if it's a static file request
    allowed_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.svg', '.ico', '.webp', '.mp3', '.wav'}
    if '.' in path:
        file_ext = '.' + path.split('.')[-1].lower()
        if file_ext in allowed_extensions:
            file_path = FRONTEND_DIST / path
            if file_path.exists() and file_path.is_file():
                return FileResponse(str(file_path))
    
    # Don't serve index.html for API routes, docs, or assets
    if (path.startswith("api/") or 
        path.startswith("docs") or 
        path.startswith("openapi.json") or
        path.startswith("assets/") or
        path.startswith("static/")):
        raise HTTPException(status_code=404, detail="Not found")
    
    # Serve index.html for all other routes (React Router will handle them)
    index_file = FRONTEND_DIST / "index.html"
    if index_file.exists():
        return FileResponse(str(index_file))
    else:
        raise HTTPException(status_code=404, detail="Frontend not built")

if __name__ == "__main__":
    import uvicorn
    import os
    # Use Railway's standard port 3000 in production, 8000 for local dev
    port = int(os.environ.get("PORT", 3000 if os.environ.get("RAILWAY_ENVIRONMENT") else 8000))
    uvicorn.run(app, host="0.0.0.0", port=port) 