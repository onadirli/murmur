from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import List, Optional
from .services.utils import Gender, State, IncomeLevel, EducationLevel, SentimentType


# In the interest of time, I'm creating the bare minimum schemas that I need for the frontend to work.
# There's more nested info being returned than needed, but it's better than not having any and making more requests.

#TODO: add actual schemas for each model that needs to be exposed, CREATE, READ, UPDATE, DELETE, etc.
#TODO: allow for ~~optional~~ prefetching of related models to reduce the number of requests

class Core(BaseModel):
    id: UUID4
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

class UploadCreate(BaseModel):
    upload_name: Optional[str] = None

class UploadRead(Core):
    upload_name: Optional[str] = None

class RespondentRead(Core):
    upload_id: Optional[int] = None
    age: Optional[int] = None
    gender: Gender = Gender.CHOOSE_NOT_TO_DISCLOSE
    zip_code: Optional[str] = None
    city: Optional[str] = None
    state: Optional[State] = None
    income_level: Optional[IncomeLevel] = None
    education_level: Optional[EducationLevel] = None

class QuestionRead(Core):
    question_name: str
    question_text: str



class QuestionResponseRead(Core):
    question: QuestionRead
    respondent_id: UUID4
    response_value: str


class SurveyResponseRead(Core):
    respondent: RespondentRead
    sentiment: SentimentType = SentimentType.NEGATIVE
    question_responses: List[QuestionResponseRead]

    