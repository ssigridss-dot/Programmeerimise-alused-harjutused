"""School class which stores information about courses and students."""


from course import Course
from student import Student


class School:
    """School class, do not change."""

    def __init__(self, name):
        """Initialize school object with name."""
        self.__students = []
        self.__courses = []
        self.name = name
        self.__next_id = 1

    def add_course(self, course: Course):
        """Add new course."""
        if course not in self.__courses:
            self.__courses.append(course)

    def add_student(self, student: Student):
        """Add new student."""
        if student not in self.__students:
            self.__students.append(student)
            student.set_id(self.__next_id)
            self.__next_id += 1

    def add_student_grade(self, student: Student, course: Course, grade: int):
        """Add student grade."""
        if student not in self.__students or course not in self.__courses:
            return
        student.add_grade(course, grade)
        course.add_grade(student, grade)

    def get_students(self) -> list[Student]:
        """Return student list."""
        return self.__students.copy()

    def get_courses(self) -> list[Course]:
        """Return course list."""
        return self.__courses.copy()

    def get_students_ordered_by_average_grade(self) -> list[Student]:
        """Return students ordered by average grade."""
        return sorted(self.__students,
                      key=lambda student: student.get_average_grade(), reverse=True)