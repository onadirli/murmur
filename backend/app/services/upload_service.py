from sqlalchemy.orm import Session
from .. import models
from uuid import UUID
import csv
import io
from .utils import (
    format_state, format_zipcode, format_education_level,
    format_gender, format_income_level, SentimentType
)



# TODO: break this into smaller functions, refactor to be more flexible

def process_upload(upload_id: UUID, db: Session):
    # Get the upload from database
    upload = db.query(models.Upload).filter(models.Upload.id == upload_id).first()
    
    if not upload:
        return None
        
    # Read and parse the CSV file
    file_content = io.StringIO(upload.upload_file.decode('utf-8'))
    reader = csv.DictReader(file_content)
    
    # Create a survey for the upload
    survey = models.Survey(
        name=f"{upload.upload_name}",
        upload_id=upload_id
    )
    db.add(survey)
    db.flush()  # Get the survey ID without committing
    
    # Create 5 questions
    questions = []
    for i in range(1, 6):
        question = models.Question(
            question_name=f"q{i}",
            question_text=f"Question {i}"
        )
        questions.append(question)
        db.add(question)
    db.flush()  # Get question IDs without committing
    
    # Associate questions with survey
    for question in questions:
        survey.questions.append(question)
    
    # Process each row in the CSV
    for row in reader:
        # Create respondent
        respondent = models.Respondent(
            upload_id=(row['id']) if row['id'] else None,
            age=int(row['age']) if row['age'] else None,
            gender=format_gender(row['gender']) if row['gender'] else None,
            zip_code=format_zipcode(row['zip_code']) if row['zip_code'] else None,
            city=row['city'] if row['city'] else None,
            state=format_state(row['state']) if row['state'] else None,
            income_level=format_income_level(row['income']) if row['income'] else None,
            education_level=format_education_level(row['education_level']) if row['education_level'] else None
        )
        db.add(respondent)
        db.flush()  # Get respondent ID without committing
        
        # Create survey response
        survey_response = models.SurveyResponse(
            survey_id=survey.id,
            respondent_id=respondent.id,
            sentiment=SentimentType(row['sentiment_label']) if row['sentiment_label'] else SentimentType.NEUTRAL
        )
        db.add(survey_response)
        db.flush()  # Get survey_response ID before creating question responses
        
        # Create question responses
        for i, question in enumerate(questions, 1):
            # Determine if this is a rating or open-ended question based on the column name
            rating_key = f'q{i}_rating'
            open_key = f'q{i}_open'
            
            # Get the response value from the appropriate column
            response_value = row.get(rating_key, '') if rating_key in row else row.get(open_key, '')
            
            question_response = models.QuestionResponse(
                survey_id=survey.id,
                question_id=question.id,
                survey_response_id=survey_response.id,
                respondent_id=respondent.id,
                response_value=response_value
            )
            db.add(question_response)
    
    # Commit all changes
    db.commit()
    
    return upload

