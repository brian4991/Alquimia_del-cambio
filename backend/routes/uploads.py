"""
Routes for file uploads
"""
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import shutil
import os
from auth import get_current_admin_user
from models import User

router = APIRouter(tags=["uploads"])

# Directory for audio files
AUDIO_UPLOAD_DIR = Path("frontend/public/audio")
AUDIO_UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload/audio")
async def upload_audio(
    file: UploadFile = File(...),
    current_admin: User = Depends(get_current_admin_user)
):
    """Upload an audio file (MP3 only)"""
    
    # Validate file type
    if not file.filename.endswith('.mp3'):
        raise HTTPException(status_code=400, detail="Only MP3 files are allowed")
    
    # Generate safe filename
    safe_filename = file.filename.replace(" ", "_")
    file_path = AUDIO_UPLOAD_DIR / safe_filename
    
    # Save file
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")
    
    # Return the filename (will be stored in database)
    return {
        "filename": safe_filename,
        "path": f"/audio/{safe_filename}",
        "message": "File uploaded successfully"
    }

@router.delete("/upload/audio/{filename}")
async def delete_audio(
    filename: str,
    current_admin: User = Depends(get_current_admin_user)
):
    """Delete an audio file"""
    
    file_path = AUDIO_UPLOAD_DIR / filename
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    try:
        os.remove(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete file: {str(e)}")
    
    return {"message": "File deleted successfully"}

