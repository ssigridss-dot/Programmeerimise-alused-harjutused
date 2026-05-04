class Book:
    """
    Represents a book.
    """

    count = 0  # class variable

    def __init__(self, title, pages):
        """
        Constructor for Book.
        """
        self.title = title
        self.pages = pages
        Book.count += 1

    def read(self):
        """
        Simulates reading the book.
        """
        return f"Reading {self.title}"

    def info(self):
        """
        Returns book information.
        """
        return f"{self.title}, {self.pages} pages"


class SpecialBook(Book):
    """
    Inherited Book class.
    """

    def __init__(self, title="Default Book", pages=100, author="Randla"):
        """
        Constructor with default values.
        """
        super().__init__(title, pages)
        self.author = author

    def author_info(self):
        """
        Returns author info.
        """
        return f"Author: {self.author}"


if __name__ == "__main__":
    b = SpecialBook("Python", 300)
    print(b.read())
    print(b.info())
    print(b.author_info())
    print(Book.count)