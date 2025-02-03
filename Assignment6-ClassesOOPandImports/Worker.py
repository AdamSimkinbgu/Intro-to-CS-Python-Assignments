from abc import abstractmethod

from Person import Person


class Worker(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)

    def __str__(self):
        return f'Name:{self._name},Age:{self._age},Job:'

    @abstractmethod
    def work(self, shift):
        pass

# print('name:{},age:{}'.format('adam',18))