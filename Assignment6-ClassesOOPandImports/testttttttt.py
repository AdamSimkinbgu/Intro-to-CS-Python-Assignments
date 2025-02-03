from abc import ABC, abstractmethod
import PyBarException


class Person(ABC):
    def __init__(self, name, age):
        if not name or isinstance(name, str) is False:
            raise PyBarException.InvalidInputException("Name can not be empty and must be str")
        if not isinstance(age, int):
            raise PyBarException.InvalidInputException("Age must be an integer")
        if age < 18:
            raise PyBarException.InvalidInputException("Must be older then 18")
        if not isinstance(self, Adam):
            raise PyBarException.InvalidInputException('You are not allowed')
        self._name = name
        self._age = age


    def __str__(self):
        return f'Name:{self._name},Age:{self._age}'

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


class Adam(Person):
    def __init__(self, name, age):
        try:
            Person.__init__(self, name, age)
        except PyBarException.InvalidInputException as e:
            print(e)
        except THEENDOFTHEWORLD as e:
            print(e)

class Mai(Person):
    def __init__(self, name, age):
        try:
            Person.__init__(self, name, age)
        except PyBarException.InvalidInputException as e:
            print(e)
        except THEENDOFTHEWORLD as e:
            print(e)


class THEENDOFTHEWORLD(Exception):
    def __init__(self, message):
        self.message = message

def is_the_sky_blue():
    raise THEENDOFTHEWORLD('The sky is not blue')

Adam('adam', 18)
Mai('mai', 18)


class Animal(ABC):
    def __init__(self, name, age, food, weight, height, x, y, directionH):
        self.name = name
        self.age = age
        self.food = food
        self.weight = weight
        self.height = height
        self.x = x
        self.y = y
        self.directionH = directionH


class Fish(Animal, ABC):
    def __init__(self, name, age, food, weight, height, x, y, directionH):
        Animal.__init__(self, name, age, food, weight, height, x, y, directionH)

    def swim(self):
        print('I am swimming')


class Scalar(Fish):
    def __init__(self, name, age, food, weight, height, x, y, directionH):
        Fish.__init__(self, name, age, food, weight, height, x, y, directionH)

    def swim(self):
        print('I am swimming')

Scalar('scalar', 1, 'fish', 1, 1, 1, 1, 'north').swim()