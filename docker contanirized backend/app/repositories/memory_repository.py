from app.models.student import Student
from app.repositories.repository import StudentRepository


class MemoryStudentRepository(StudentRepository):

    def __init__(self):
        self.students = []

    def get_all_students(self):
        return self.students

    def get_student_by_id(self, student_id: int):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def create_student(self, student: Student):
        self.students.append(student)
        return student

    def delete_student(self, student_id: int):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                return True
        return False