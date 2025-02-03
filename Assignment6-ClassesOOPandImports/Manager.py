from Group import Group
from Person import Person
from Worker import Worker

class Manager(Worker):
    def __init__(self, name, age):
        Person.__init__(self, name, age)
        self.__job = "Manager"

    def __str__(self):
        return f'Name:{self._name},Age:{self._age},Job:{self.__job}'

    def work(self, shift):
        for table in shift.table_list:
            if table.is_empty():
                continue
            shift.add_money(table.pay()[0])
            shift.add_tip(table.pay()[1])
            print(f"Thank you {Group.get_customers_string(table.group)}! You paid {table.pay()[0] + table.pay()[1]}. See you next time!")
        print(f"This is the end of the shift:\n{shift.shift_number}\nTotal money: {shift.get_money(self)}, total tip: {shift.get_tip(self)}")





# m = Manager("tom", 18)
# print(m)
