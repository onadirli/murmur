from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

from . import models
from .database import engine
from .routers import surveys, uploads, questions

# Create tables
models.Base.metadata.create_all(bind=engine)

# Load environment variables
load_dotenv()

app = FastAPI(title="Whispr API")

frontend_port = os.getenv("FRONTEND_PORT", "3000")
frontend_url = os.getenv("FRONTEND_URL", f"http://localhost:{frontend_port}")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(surveys.router, prefix="/surveys", tags=["surveys"])
app.include_router(uploads.router, prefix="/uploads", tags=["uploads"])
app.include_router(questions.router, prefix="/questions", tags=["questions"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Todo API"}
