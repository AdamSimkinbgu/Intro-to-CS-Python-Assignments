import Group
from Person import Person
from Worker import Worker

class Waiter(Worker):
    def __init__(self, name, age):
        Person.__init__(self, name, age)
        self._job = "Waiter"

    def __str__(self):
        return f'Name:{self._name},Age:{self._age},Job:{self._job}'

    def work(self, shift):
        for table in shift.table_list:
            if table.is_empty():
                continue
            print(f"Hey {table.group.get_customers_string()}! My name is {self.get_name()} and I'm your waiter.")
            table.order(shift.menu)
            print()

