import PyBarException
from Person import Person
from Worker import Worker

class Hostess(Worker):
    def __init__(self, name, age):
        Person.__init__(self, name, age)
        self._job = "Hostess"

    def __str__(self):
        return f'Name:{self._name},Age:{self._age},Job:{self._job}'

    def work(self, shift):
        left_out = True
        for group in sorted(shift.groups_list, reverse=True):
            for empty_table in shift.table_list:
                if empty_table.is_empty() and len(group) <= len(empty_table):
                    try:
                        empty_table.seat(group)
                        left_out = False
                        print(f'{group.get_customers_string()} you can seat on table {empty_table.number} please')
                    except PyBarException.TooSmallTableException:
                        continue
                    break
            if left_out == True:
                print(f"Sorry {group.get_customers_string()}, we don't have place for {len(group)}")
            left_out = True

# q = Hostess("larry", 66)
# print(q)