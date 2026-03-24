"""Simple class."""


class Student:
    """Student class."""

    def __init__(self, name, finished=False):
        """Construct a student instance."""
        self.name = name
        self.finished = finished


if __name__ == '__main__':
    student = Student("John")
    print(student.name)  # John
    print(student.finished)  # False