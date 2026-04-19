"""Course class with name and grades."""


class Course:
    """Course class."""

    def __init__(self, name: str):
        """Initialize course object with name."""
        self.name = name
        self.__grades = []

    def add_grade(self, student, grade: int):
        """Add student grade to course."""
        self.__grades.append((student, grade))

    def get_grades(self) -> list[tuple[str, int]]:
        """Return a list of tuples where first is student object and second is their grade."""
        return self.__grades.copy()

    def get_average_grade(self):
        """Return average grade in course."""
        if not self.__grades:
            return -1
        return sum(grade for _, grade in self.__grades) / len(self.__grades)

    def __repr__(self):
        """Return course name."""
        return self.name