import PyBarException
from Group import Group


class Table:
    def __init__(self, number, max_capacity):
        if not isinstance(number, int):
            raise PyBarException.InvalidInputException('Table number that was provided is of a foreign type: expected [int]')
        if number < 0:
            raise PyBarException.InvalidInputException('Table number can not be lower then 1!')
        self.number = number
        self.max_capacity = max_capacity
        self.group = None
        self.bill = {}

    def __repr__(self):
        return str(self.__str__())

    def __str__(self):
        return f'Table number {self.number} has {self.max_capacity} seats.'

    def __len__(self):
        return self.max_capacity

    def __lt__(self, other):
        if self is other:
            return f'You are trying to compare the same table'
        if isinstance(self, Table) and isinstance(other, Table):
            if self.max_capacity < other.max_capacity:
                return f'Yes, table {other.number} is larger then table {self.number} in size'
            elif self.max_capacity > other.max_capacity:
                return f'Table {other.number} is smaller then table {self.number} in size'
            return f'Table {other.number} is the same size as table {self.number} in size'
        return f'{other} is not of Table class and can not be compared to other tables!'

    def __le__(self, other):
        if self is other:
            return f'You are trying to compare the same table'
        if isinstance(self, Table) and isinstance(other, Table):
            if other.max_capacity >= self.max_capacity:
                return f'Table {other.number} is larger then table {self.number} in size'

    def __eq__(self, other):
        if self is other:
            return f'You are trying to check equality of one table to itself'
        if isinstance(self, Table) and isinstance(other, Table):
            if self.max_capacity == other.max_capacity:
                return True
            return False
        raise PyBarException.InvalidInputException('The class you are trying to compare with is incompatible')

    def is_empty(self):
        if self.group != None:
            return False
        return True

    def seat(self, group):                                                             ########### FIX: RETURNING NONE
        if not isinstance(group, Group):
            raise PyBarException.InvalidInputException('You are trying to seat something that is not a group!')
        if not self.is_empty():
            raise PyBarException.OccupiedTableException('The table is not empty!')
        if len(group) > self.max_capacity:
            raise PyBarException.TooSmallTableException('The group is too large for this table and therefore cannot be seated')
        self.group = group

    def order(self, menu):
        if Table.is_empty(self):
            raise PyBarException.EmptyTableException("The table given is empty")
        GroupsOrder = self.group.get_order()
        for item in GroupsOrder:
            if item in menu:
                self.bill[item] = menu[item] * GroupsOrder.get(item)
            else:
                print(f"Sorry we don't have {item}")
        print('Your bill is:')
        for product in self.bill:
            print(f"{product}..........{self.bill[product]}")
                                                                  ################# FIX: GOING DOWN A LINE

    def pay(self):
        if Table.is_empty(self):
            raise PyBarException.EmptyTableException("The table given is empty")
        total_tip = 0
        bill_to_pay = 0
        for item_in_bill in self.bill:
            bill_to_pay += self.bill[item_in_bill]
        for customer in self.group.customer_list:
            total_tip += customer.get_tip() * (bill_to_pay / len(self.group))
        return bill_to_pay, total_tip


