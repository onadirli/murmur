from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..services.upload_service import process_upload

router = APIRouter()

@router.post("/", response_model=schemas.UploadRead)
async def create_upload(
    file: UploadFile = File(...),
    metadata: schemas.UploadCreate = None,
    db: Session = Depends(get_db)
):
    # Read the file content
    file_content = await file.read()
    
    # Get the upload name from metadata or filename
    upload_name = metadata.upload_name if metadata and metadata.upload_name else file.filename
    
    # Check if upload name already exists
    existing_upload = db.query(models.Upload).filter(models.Upload.upload_name == upload_name).first()
    if existing_upload:
        raise HTTPException(
            status_code=400,
            detail=f"Upload with name '{upload_name}' already exists"
        )
    
    # Create upload record
    upload = models.Upload(
        upload_name=upload_name,
        upload_file=file_content,
    )
    
    db.add(upload)
    db.commit()
    db.refresh(upload)
    
    process_upload(upload.id, db)

    return upload
