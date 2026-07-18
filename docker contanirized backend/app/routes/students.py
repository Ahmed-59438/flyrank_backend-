from fastapi import APIRouter, HTTPException
from app.models.student import Student
from app.services.student_service import StudentService

router = APIRouter(prefix="/students", tags=["Students"])

service = StudentService()


@router.get("/")
def get_all_students():
    return service.get_all_students()


@router.get("/{student_id}")
def get_student(student_id: int):
    student = service.get_student_by_id(student_id)

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return student


@router.post("/")
def create_student(student: Student):
    return service.create_student(student)


@router.delete("/{student_id}")
def delete_student(student_id: int):
    deleted = service.delete_student(student_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "Student deleted successfully"}