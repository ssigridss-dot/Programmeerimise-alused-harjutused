"""Student class with student name and grades."""


class Student:
    """Student class, do not change."""

    def __init__(self, name: str):
        """Initialize student object with name."""
        self.name = name
        self.__grades = []
        self.__id = None

    def set_id(self, id: int):
        """Set student id."""
        if self.__id is None:
            self.__id = id

    def get_id(self) -> int:
        """Return student id."""
        return self.__id

    def add_grade(self, course, grade: int):
        """Add grades to student."""
        self.__grades.append((course, grade))

    def get_grades(self) -> list[tuple[str, int]]:
        """Return student grades."""
        return self.__grades.copy()

    def get_average_grade(self):
        """Return student average grade."""
        if not self.__grades:
            return -1
        return sum(grade for _, grade in self.__grades) / len(self.__grades)

    def __repr__(self) -> str:
        """Return student name."""
        return self.name