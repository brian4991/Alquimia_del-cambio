import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from database import create_tables, get_db
from init_data import init_database
from routes import auth, modules, legacy, api, admin_import, create_modules, uploads
import migrate_theme_cards

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent
FRONTEND_DIST = PROJECT_ROOT / "frontend" / "dist"

# FastAPI app
app = FastAPI(
    title="Cambio de Paradigma",
    version="1.0.0",
    description="Aplicación de transformación personal y desarrollo emocional"
)

# Session middleware (required for OAuth)
SECRET_KEY = os.environ.get("SECRET_KEY", "your-secret-key-here-change-in-production")
# Determine if we're in production (HTTPS)
is_production = os.environ.get("RAILWAY_ENVIRONMENT") or os.environ.get("PRODUCTION", "").lower() == "true"
app.add_middleware(
    SessionMiddleware, 
    secret_key=SECRET_KEY,
    session_cookie="alquimia_session",
    max_age=3600,
    same_site="lax",  # Use "lax" to allow cross-site requests for OAuth
    https_only=is_production  # Set to True in production with HTTPS
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000", 
        "http://localhost:5173",
        "http://localhost:5174",
        "https://alquimia-del-cambio.vercel.app",
        "https://alquimiadel-cambio-production.up.railway.app",
        "https://www.nicoleramirezpsicoach.com",
        "https://nicoleramirezpsicoach.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount audio files directory
FRONTEND_PUBLIC_AUDIO = PROJECT_ROOT / "frontend" / "public" / "audio"
if FRONTEND_PUBLIC_AUDIO.exists():
    app.mount("/audio", StaticFiles(directory=str(FRONTEND_PUBLIC_AUDIO)), name="audio")

# Mount static files (frontend build) - only if the directory exists
if FRONTEND_DIST.exists():
    # Mount assets directory for JS/CSS files
    assets_dir = FRONTEND_DIST / "assets"
    if assets_dir.exists():
        app.mount("/assets", StaticFiles(directory=str(assets_dir)), name="assets")
    
    # Mount other static files at root level
    app.mount("/static", StaticFiles(directory=str(FRONTEND_DIST)), name="static")

# Include routers
app.include_router(auth.router, prefix="/auth")  # Auth routes with /auth prefix
app.include_router(modules.router)  # No prefix for modules (to keep existing frontend working)
app.include_router(api.router, prefix="/api")  # API prefix for card operations
app.include_router(admin_import.router)  # Admin import routes
app.include_router(create_modules.router)  # Create modules routes
app.include_router(migrate_theme_cards.router)  # Theme cards migration
app.include_router(uploads.router, prefix="/api")  # File uploads
app.include_router(legacy.router)

def run_migrations():
    """Run database migrations for missing columns"""
    from sqlalchemy import text
    db = next(get_db())
    try:
        # Check if we're using PostgreSQL or SQLite
        dialect = db.bind.dialect.name
        
        if dialect == 'postgresql':
            # PostgreSQL syntax
            db.execute(text("ALTER TABLE modules ADD COLUMN IF NOT EXISTS meditation_video_url TEXT"))
        else:
            # SQLite - check if column exists first
            result = db.execute(text("PRAGMA table_info(modules)"))
            columns = [row[1] for row in result.fetchall()]
            if 'meditation_video_url' not in columns:
                db.execute(text("ALTER TABLE modules ADD COLUMN meditation_video_url TEXT"))
        
        db.commit()
        print("Migrations completed successfully")
    except Exception as e:
        print(f"Migration warning (may be OK if column exists): {e}")
        db.rollback()
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    """Initialize database and create tables on startup"""
    create_tables()
    run_migrations()  # Run migrations before init_database
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
        "message": "Welcome to Cambio de Paradigma API",
        "version": "1.0.0",
        "docs": "/docs"
    }

# TEMPORARY ENDPOINT - Remove after migration
@app.post("/admin/migrate-sub-question-index")
def migrate_sub_question_index_endpoint():
    """
    Temporary endpoint to run sub_question_index migration
    Changes column from INTEGER to TEXT to support new exercise format
    """
    from sqlalchemy import text
    from database import engine
    
    try:
        with engine.connect() as conn:
            with conn.begin():
                # Check current column type
                result = conn.execute(text("""
                    SELECT column_name, data_type 
                    FROM information_schema.columns 
                    WHERE table_name = 'user_sub_question_responses' 
                    AND column_name = 'sub_question_index'
                """))
                
                current_col = result.fetchone()
                if not current_col:
                    return {"error": "Column not found", "status": "failed"}
                
                current_type = current_col[1]
                
                if current_type == 'text' or current_type == 'character varying':
                    return {
                        "message": "Migration already completed - column is already TEXT",
                        "current_type": current_type,
                        "status": "already_done"
                    }
                
                # Alter column type
                conn.execute(text("""
                    ALTER TABLE user_sub_question_responses 
                    ALTER COLUMN sub_question_index TYPE TEXT 
                    USING sub_question_index::TEXT
                """))
                
                # Verify
                result = conn.execute(text("""
                    SELECT column_name, data_type 
                    FROM information_schema.columns 
                    WHERE table_name = 'user_sub_question_responses' 
                    AND column_name = 'sub_question_index'
                """))
                
                new_col = result.fetchone()
                
                return {
                    "message": "Migration completed successfully!",
                    "old_type": current_type,
                    "new_type": new_col[1],
                    "status": "success"
                }
                
    except Exception as e:
        return {
            "error": str(e),
            "status": "failed"
        }

# TEMPORARY ENDPOINT - Remove after migration
@app.post("/admin/migrate-card-responses")
def migrate_card_responses_endpoint():
    """
    Temporary endpoint to create card_responses table
    For storing user responses to card-based exercises
    """
    from database import create_tables
    from sqlalchemy import text
    from database import engine
    
    try:
        # Create all missing tables
        create_tables()
        
        # Verify table exists
        with engine.connect() as conn:
            result = conn.execute(text("""
                SELECT table_name FROM information_schema.tables 
                WHERE table_name='card_responses'
            """))
            
            if result.fetchone():
                # Get table structure
                result = conn.execute(text("""
                    SELECT column_name, data_type 
                    FROM information_schema.columns 
                    WHERE table_name = 'card_responses'
                    ORDER BY ordinal_position
                """))
                columns = result.fetchall()
                
                return {
                    "message": "Table 'card_responses' created successfully!",
                    "columns": [{"name": col[0], "type": col[1]} for col in columns],
                    "status": "success"
                }
            else:
                return {
                    "error": "Failed to create table 'card_responses'",
                    "status": "failed"
                }
                
    except Exception as e:
        return {
            "error": str(e),
            "status": "failed"
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
    allowed_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.svg', '.ico', '.webp', '.mp3', '.wav', '.mp4', '.mov', '.webm'}
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