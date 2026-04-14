from typing import List, Any
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Response,
    status,
)

from sqlalchemy.orm import Session
from app.api import deps
from app import (
    crud,
    schemas,
)
from app.models.user import User
from app.schemas.responses import APIResponse

router = APIRouter(prefix='/students', tags=['Students'])


@router.get('', response_model=APIResponse[List[schemas.StudentInDB]])
def get_students(
    *,
    db: Session = Depends(deps.get_db),
    commons: deps.CommonQueryParams = Depends(),
    current_user: User = Depends(deps.get_current_active_user),
):
    students = crud.student.get_multi(db, skip=commons.skip, limit=commons.limit)
    return APIResponse(data=students)


@router.get('/{student_id}', response_model=APIResponse[schemas.StudentInDB])
def get_student(
    *,
    db: Session = Depends(deps.get_db),
    student_id: int,
    current_user: User = Depends(deps.get_current_active_user),
):
    student = crud.student.get(db, student_id)

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {student_id} does not exist."
        )
    return APIResponse(data=student)


@router.post('', response_model=APIResponse[schemas.StudentInDB], status_code=status.HTTP_201_CREATED)
def create_student(
    *,
    db: Session = Depends(deps.get_db),
    student_in: schemas.StudentCreate,
    current_user: User = Depends(deps.get_current_active_admin),
):
    if not crud.nationality.get(db, student_in.nationality_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nationality with id {student_in.nationality_id} not found."
        )
    student = crud.student.create(db, obj_in=student_in)
    return APIResponse(data=student, message="Student created successfully")


@router.put('/{student_id}', response_model=APIResponse[schemas.StudentInDB])
def update_student(
    *,
    db: Session = Depends(deps.get_db),
    student_id: int,
    student_in: schemas.StudentUpdate,
    current_user: User = Depends(deps.get_current_active_admin),
):
    student = crud.student.get(db, student_id)

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {student_id} does not exist."
        )
    if not crud.nationality.get(db, student_in.nationality_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Nationality with id {student_in.nationality_id} not found."
        )
    student = crud.student.update(db, db_obj=student, obj_in=student_in)

    return APIResponse(data=student, message="Student updated successfully")


@router.delete('/{student_id}', response_model=APIResponse[None], status_code=status.HTTP_200_OK)
def delete_student(
    *,
    db: Session = Depends(deps.get_db),
    student_id: int,
    current_user: User = Depends(deps.get_current_active_admin),
):
    student = crud.student.get(db, student_id)

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id {student_id} does not exist."
        )

    if student.registrations:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Cannot delete this student because, it has data depends on it."
        )

    crud.student.remove(db, id=student_id)

    return APIResponse(message="Student deleted successfully")
