from fastapi import APIRouter
from app.api.api_v1.routes import (
    auth,
    grade,
    registration,
    subject,
    school_year,
    student,
    nationality,
)

api_router = APIRouter()

api_router.include_router(auth.router, tags=["Authentication"])
api_router.include_router(grade.router, tags=["Grades"])
api_router.include_router(subject.router, tags=["Subjects"])
api_router.include_router(school_year.router, tags=["Academic Years"])
api_router.include_router(student.router, tags=["Students"])
api_router.include_router(registration.router, tags=["Registrations"])
api_router.include_router(nationality.router, tags=["Nationalities"])