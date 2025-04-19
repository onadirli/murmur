from sqlalchemy import Column, Integer, String, DateTime, UUID, ForeignKey, Enum, Table, LargeBinary
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime
from uuid import uuid4
from .services.utils import Gender, State, IncomeLevel, EducationLevel, SentimentType


class Core(Base):
    __abstract__ = True

    id = Column(UUID, primary_key=True, index=True, default=uuid4)
    created_at = Column(DateTime, default=datetime.now)

class Upload(Core):
    __tablename__ = "uploads"

    upload_name = Column(String, nullable=True, unique=True)
    upload_file = Column(LargeBinary, nullable=True)


class Respondent(Core):
    __tablename__ = "respondents"

    upload_id = Column(Integer, nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(Enum(Gender), default=Gender.CHOOSE_NOT_TO_DISCLOSE)
    zip_code = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(Enum(State), nullable=True)
    income_level = Column(Enum(IncomeLevel), nullable=True)
    education_level = Column(Enum(EducationLevel), nullable=True)




# table for many-to-many relationship between Survey and Question
# each survey can have multiple questions and each question can be part of multiple surveys
survey_questions = Table(
    'survey_questions',
    Base.metadata,
    Column('survey_id', UUID, ForeignKey('surveys.id'), primary_key=True),
    Column('question_id', UUID, ForeignKey('questions.id'), primary_key=True)
)

class Survey(Core):
    __tablename__ = "surveys"

    name = Column(String, index=True, nullable=False, unique=True)
    upload_id = Column(UUID, ForeignKey("uploads.id"))
    questions = relationship("Question", secondary=survey_questions, back_populates="surveys")

# TODO: add question type, for ex. open-ended, int, multiple choice, etc.
class Question(Core):
    __tablename__ = "questions"

    question_name = Column(String, index=True, nullable=False, unique=True)
    question_text = Column(String, index=True, default="")
    surveys = relationship("Survey", secondary=survey_questions, back_populates="questions")

class SurveyResponse(Core):
    __tablename__ = "responses"

    survey_id = Column(UUID, ForeignKey("surveys.id"))
    respondent_id = Column(UUID, ForeignKey("respondents.id"))
    sentiment = Column(Enum(SentimentType), default=SentimentType.NEUTRAL)
    
    survey = relationship("Survey")
    respondent = relationship("Respondent")
    question_responses = relationship("QuestionResponse", back_populates="survey_response")

# TODO: restrict response_value type depending on question type
class QuestionResponse(Core):
    __tablename__ = "question_responses"

    survey_id = Column(UUID, ForeignKey("surveys.id"))
    question_id = Column(UUID, ForeignKey("questions.id"))
    survey_response_id = Column(UUID, ForeignKey("responses.id"))
    respondent_id = Column(UUID, ForeignKey("respondents.id"))

    response_value = Column(String, index=True, default="")
    
    survey = relationship("Survey")
    question = relationship("Question")
    survey_response = relationship("SurveyResponse", back_populates="question_responses")
    respondent = relationship("Respondent")
