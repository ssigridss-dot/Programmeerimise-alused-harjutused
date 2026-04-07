"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    STATUS_ACTIVE = "Active"
    STATUS_EXPELLED = "Expelled"
    STATUS_FINISHED = "Finished"
    STATUS_INACTIVE = "Inactive"

    def __init__(self, name: str, id: int):
        """Create constructor."""
        self.__id = id
        self.__name = name
        self.__status = Student.STATUS_ACTIVE

    def get_id(self) -> int:
        """Return student`s id."""
        return self.__id

    def set_name(self, name: str) -> None:
        """Set the name of the student."""
        self.__name = name

    def get_name(self) -> str:
        """Return student`s name."""
        return self.__name

    def set_status(self, status: str) -> None:
        """Set the student`s status only if given status is correct."""
        allowed_statuses = [Student.STATUS_ACTIVE, Student.STATUS_EXPELLED, Student.STATUS_FINISHED,
                            Student.STATUS_INACTIVE]
        if status in allowed_statuses:
            self.__status = status

    def get_status(self) -> str:
        """Return student`s status."""
        return self.__status


if __name__ == '__main__':
    student1 = Student("Tiit", 1)
    print(student1.get_status())
    student1.set_status("Lahkunud")
    print(student1.get_status())
    student1.set_status("finished")
    print(student1.get_status())
    student1.set_status(Student.STATUS_FINISHED)
    print(student1.get_status())
