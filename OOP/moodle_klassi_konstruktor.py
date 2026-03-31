"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """Construct class Person with first name, last name and age."""
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        """Construct class Student with first name, last name and age."""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    # empty usage
    empty_object = Empty()
    # 3 x person usage
    p1 = Person()
    p1.firstname = "Tiit"
    p1.lastname = "Sukk"
    p1.age = 5
    p2 = Person()
    p2.firstname = "Teet"
    p2.lastname = "Tukk"
    p2.age = 15
    p3 = Person()
    p3.firstname = "Peep"
    p3.lastname = "Lukk"
    p3.age = 25
    # 3 x student usage
    s1 = Student("Kerly", "Ritsu", 22)
    s2 = Student("Mari", "Lill", 42)
    s3 = Student("Mati", "Murakas", 35)
