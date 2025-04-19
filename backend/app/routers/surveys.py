from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from typing import List

from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.get("/", response_model=List[schemas.SurveyResponseRead])
def get_surveys(db: Session = Depends(get_db)):
    responses = (
        db.query(models.SurveyResponse)
        .options(
            joinedload(models.SurveyResponse.respondent),
            joinedload(models.SurveyResponse.question_responses)
            .joinedload(models.QuestionResponse.question)
        )
        .all()
    )
    return responses

@router.get("/{survey_name}", response_model=List[schemas.SurveyResponseRead])
def get_survey(survey_name: str, db: Session = Depends(get_db)):
    survey = db.query(models.Survey).filter(models.Survey.name == survey_name).first()
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey not found")
    
    responses = (
        db.query(models.SurveyResponse)
        .filter(models.SurveyResponse.survey_id == survey.id)
        .options(
            joinedload(models.SurveyResponse.respondent),
            joinedload(models.SurveyResponse.question_responses)
            .joinedload(models.QuestionResponse.question)
        )
        .all()
    )
    return responses

