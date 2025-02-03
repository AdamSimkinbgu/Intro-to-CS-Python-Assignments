import PyBarException
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age):
        if not name or isinstance(name, str) is False:
            raise PyBarException.InvalidInputException("Name can not be empty and must be str")
        if not isinstance(age, int):
            raise PyBarException.InvalidInputException("Age must be an integer")
        if age < 18:
            raise PyBarException.InvalidInputException("Must be older then 18")
        self._name = name
        self._age = age

    @abstractmethod
    def __str__(self):
        return f'Name:{self._name},Age:{self._age}'

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age
