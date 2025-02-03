import PyBarException
from Person import Person

class Customer(Person):
    def __init__(self, name, age, tip=0.0):
        Person.__init__(self, name, age)
        if not isinstance(tip, float) or tip < 0:
            raise PyBarException.InvalidInputException("Tip must be a number higher then zero")
        self.tip = tip

    def __repr__(self):
        return self.get_name()

    def __str__(self):
        return f'Name:{self._name},Age:{self._age},Tip:{round(self.tip * 100, 2)}%'

    def __len__(self):
        return len(self._name)

    def get_tip(self):
        return self.tip


