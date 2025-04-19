from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List
from uuid import UUID

from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.get("/{question_id}/", response_model=List[schemas.QuestionResponseRead])
def get_question_responses(question_id: UUID, db: Session = Depends(get_db)):
    question = db.query(models.Question).filter(models.Question.id == question_id).first()
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    
    responses = (
        db.query(models.QuestionResponse)
        .filter(models.QuestionResponse.question_id == question_id)
        .options(
            joinedload(models.QuestionResponse.question)
        )
        .all()
    )
    return responses
