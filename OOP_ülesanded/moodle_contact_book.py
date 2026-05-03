"""Contact book."""


class Person:
    """Person class."""

    def __init__(self, firstname: str, lastname: str, phone_number: str):
        """Person constructor."""
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number

    def get_full_name(self) -> str:
        """
        Get full name of the person.

        Return firstname and lastname separated by space.
        If the lastname is empty, then return only the firstname.
        """
        if self.lastname == "":
            return self.firstname
        return self.firstname + " " + self.lastname


class ContactBook:
    """Contact book class."""

    def __init__(self):
        """Contact book constructor."""
        self.contacts = []

    def add_person_to_contacts(self, person: Person) -> None:
        """Add person to contact book if phone number and firstname are not empty strings."""
        if person.firstname != "" and person.phone_number != "":
            self.contacts.append(person)

    def find_contact_by_number(self, number) -> Person:
        """
        Return person who has the given number.

        If there are several people with the given number, return the first.
        If there is no person with the given number, return None.
        """
        for person in self.contacts:
            if person.phone_number == number:
                return person
        return None

    def get_sorted_contacts(self) -> list:
        """Sort contacts alphabetically by full name."""
        return sorted(self.contacts, key=lambda p: p.get_full_name())


if __name__ == '__main__':
    book = ContactBook()

    p1 = Person("Mari", "Kask", "123")
    p2 = Person("Jaan", "Tamm", "456")
    p3 = Person("Anna", "", "789")
    p4 = Person("", "NoName", "000")  # ei lisata (firstname tühi)

    book.add_person_to_contacts(p1)
    book.add_person_to_contacts(p2)
    book.add_person_to_contacts(p3)
    book.add_person_to_contacts(p4)

    print("Kõik kontaktid:")
    for p in book.contacts:
        print(p.get_full_name(), "-", p.phone_number)

    print("\nOtsi numbri järgi (456):")
    found = book.find_contact_by_number("456")
    if found:
        print(found.get_full_name())
    else:
        print("Ei leitud")

    print("\nSorteeritud kontaktid:")
    for p in book.get_sorted_contacts():
        print(p.get_full_name(), "-", p.phone_number)