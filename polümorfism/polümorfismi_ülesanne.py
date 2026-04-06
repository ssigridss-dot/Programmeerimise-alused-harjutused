class Animal:
    """Animal class."""

    def __init__(self, name="None", is_pet=False):
        """
        Class constructor.

        :param name: animal name
        :param is_pet: pet or wild?
        """
        self.name = name
        self.is_pet = is_pet

    def speak(self):
        return "I cannot"

    def greet(self):
        return self.name + " greets you!"

    def is_friendly(self):
        return self.is_pet

    def __str__(self):
        return self.name


class Cat(Animal):
    """Class Cat extends class Animal"""

    def __init__(self, name, is_pet=True):
        super().__init__(name, is_pet)

class Dog(Animal):
    """Class Dog extends class Animal"""

    def __init__(self, name, is_pet=True):
        """
        Class constructor.

        :param name: dog name
        :param is_pet: dog usually is a pet
        """
        # Overriding the base constructor, passing new values to self.is_pet and self.name
        super().__init__(name, is_pet)

    def roll(self):
        """
        Extra method, specific for this class.

        :return:
        """
        return("*rolling*")

    def speak(self):
        """
        Overriding the base method.
        By default it returns "I cannot", we change it to return "Bark!".

        :return: Bark!
        """
        return "Bark!"


class Dolphin(Animal):
    """Class Dolphin extends class Animal."""

    # Class constructor with two more arguments
    def __init__(self, name, playful, smart):
        """
        Class constructor with two extra parameters.

        :param name:
        :param playful
        :param smart
        """
        # Overriding the base constructor, passing new value to self.name
        super().__init__(name)

        self.playful = playful
        self.smart = smart

    def is_friendly(self):
        """
        Overriding the base method.
        By default if the animal is not a pet, it isn't friendly either. However in our case,
        if the dolphin is in playful mood or smart, it will be friendly to us.

        :return: boolean
        """

        return self.smart or self.playful or super().is_friendly()

    def greet(self):
        """
        Overriding the base method.
        By default it returns "<name of the animal> greets you!". In our case it returns "*Water splash*".

        :return: *Water splash*
        """
        return "*Water splash*"

    def perform_jump(self):
        """
        Extra method, specific for this class.

        :return:
        """

        if self.playful:
            return "*Jumps*"

        elif self.smart:
            return "I will jump.. for food."

        return "No."


def speak_test(animal: Animal):
    print(animal.speak())


if __name__ == '__main__':
    animal = Animal()
    print(animal.is_pet)  # --> False
    print(animal)  # --> None
    print(animal.is_friendly())  # --> False
    print(animal.greet())  # --> None greets you!
    print(animal.speak())  # --> I cannot

    print()

    dog = Dog("Sparky")
    print(dog.is_pet)  # --> True
    print(dog)  # --> Sparky
    print(dog.is_friendly())  # --> True
    print(dog.greet())  # --> Sparky greets you!
    print(dog.speak())  # --> Bark!
    print(dog.roll())  # --> *rolling*

    print()

    dolphin = Dolphin("Steve", False, True)
    print(dolphin.is_pet)  # --> False
    print(dolphin)  # --> Steve
    print(dolphin.is_friendly())  # --> True
    print(dolphin.greet())  # --> *Water splash*
    print(dolphin.speak())  # --> I cannot
    print(dolphin.perform_jump())  # --> I will jump.. For food.

    print()

    print("Speak tests")
    speak_test(animal)
    speak_test(dog)
    speak_test(dolphin)