from abc import ABC, abstractmethod
from app.models.student import Student


class StudentRepository(ABC):

    @abstractmethod
    def get_all_students(self):
        pass

    @abstractmethod
    def get_student_by_id(self, student_id: int):
        pass

    @abstractmethod
    def create_student(self, student: Student):
        pass

    @abstractmethod
    def delete_student(self, student_id: int):
        pass