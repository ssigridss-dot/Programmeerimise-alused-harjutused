from abc import ABC, abstractmethod


class Animal(ABC):

    def sleep(self):
        print("I am going to sleep.")

    @abstractmethod
    def speak(self):
        raise NotImplemented

class Human(Animal):

    def speak(self):
        print("I can talk.")

class Snake(Animal):

    def speak(self):
        print("I can hiss.")

class Dog(Animal):

    def speak(self):
        print("I can bark.")

class Lion(Animal):

    def speak(self):
        print("I can roar.")

class Fish(Animal):

    def speak(self):
        print("Mull-mull-mull.")


human = Human()
human.speak()

snake = Snake()
snake.speak()

dog = Dog()
dog.speak()

lion = Lion()
lion.speak()

fish = Fish()
fish.speak()