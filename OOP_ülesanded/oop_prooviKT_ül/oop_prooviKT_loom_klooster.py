class Animal:
    """
    Represents an animal.
    """

    count = 0

    def __init__(self, species, age):
        """
        Constructor.
        """
        self.species = species
        self.age = age
        Animal.count += 1

    def speak(self):
        """
        Animal sound.
        """
        return "Sound"

    def info(self):
        """
        Animal info.
        """
        return f"{self.species}, {self.age}"


class PetAnimal(Animal):
    """
    Inherited Animal class.
    """

    def __init__(self, species="Dog", age=3, name="Buddy"):
        """
        Default constructor.
        """
        super().__init__(species, age)
        self.name = name

    def pet_info(self):
        """
        Pet name info.
        """
        return f"Name: {self.name}"


if __name__ == "__main__":
    a = PetAnimal()
    print(a.speak())
    print(a.info())
    print(a.pet_info())
    print(Animal.count)