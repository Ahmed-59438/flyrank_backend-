from app.repositories.repository import StudentRepository
from app.models.student import Student
from app.database import get_connection


class PostgresStudentRepository(StudentRepository):

    def get_all_students(self):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT id, name, email FROM students")

        rows = cur.fetchall()

        cur.close()
        conn.close()

        return [
            Student(id=row[0], name=row[1], email=row[2])
            for row in rows
        ]

    def get_student_by_id(self, student_id: int):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT id, name, email FROM students WHERE id = %s",
            (student_id,)
        )

        row = cur.fetchone()

        cur.close()
        conn.close()

        if row:
            return Student(
                id=row[0],
                name=row[1],
                email=row[2]
            )

        return None

    def create_student(self, student: Student):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO students (id, name, email)
            VALUES (%s, %s, %s)
            """,
            (student.id, student.name, student.email)
        )

        conn.commit()

        cur.close()
        conn.close()

        return student

    def delete_student(self, student_id: int):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "DELETE FROM students WHERE id = %s",
            (student_id,)
        )
        deleted = cur.rowcount > 0
        conn.commit()

        cur.close()
        conn.close()

        return deleted
    