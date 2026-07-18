from app.models.student import Student
from app.repositories.postgres_repository import PostgresStudentRepository


class StudentService:
    def __init__(self):
        self.repository = PostgresStudentRepository()

    def get_all_students(self):
        return self.repository.get_all_students()

    def get_student_by_id(self, student_id: int):
        return self.repository.get_student_by_id(student_id)

    def create_student(self, student: Student):
        return self.repository.create_student(student)

    def delete_student(self, student_id: int):
        return self.repository.delete_student(student_id)