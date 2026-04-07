"""Course module."""
import statistics
from typing import Dict
from student import Student

class Course:
    """Course class."""

    def __init__(self, name: str):
        """Initialize course object with name."""
        self.__name = name
        self.__grades: Dict[Student, int] = {}

    def get_grades(self):
        """Return a list of tuples where first is student object and second is their grade."""
        return list(self.__grades.items())

    def get_average_grade(self) -> float:
        """Return the average grade of all student grades."""
        if len(self.__grades) == 0:
            return -1
        return mean(self.__grades.values())

    def __repr__(self):
        return self.name