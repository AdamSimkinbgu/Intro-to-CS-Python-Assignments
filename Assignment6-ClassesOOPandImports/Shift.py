from copy import deepcopy

import PyBarException
from Customer import Customer
from Group import Group
from Hostess import Hostess
from Manager import Manager
from Table import Table
from Waiter import Waiter


class Shift:
    def __init__(self, shift_number, table_list, groups_list, workers_list, menu):
        counter = 0
        if not isinstance(shift_number, int):
            raise PyBarException.InvalidInputException('The shift number that was provided is of a foreign type: expected [int]')
        if shift_number <= 0:
            raise PyBarException.InvalidInputException('The shift number can not be lower then 1!')
        if not isinstance(table_list, list):
            raise PyBarException.InvalidInputException('The table list that was provided is of a foreign type: expected [list]')
        for worker in workers_list:
            if counter == 0:
                if not isinstance(worker, Hostess):
                    raise PyBarException.InvalidInputException('Hostess was provided incorrectly')
            if counter == 1:
                if not isinstance(worker, Waiter):
                    raise PyBarException.InvalidInputException('Waiter was provided incorrectly')
            if counter == 2:
                if not isinstance(worker, Manager):
                    raise PyBarException.InvalidInputException('Manager was provided incorrectly')
            counter += 1
        if not isinstance(groups_list, list):
            raise PyBarException.InvalidInputException('A group list was not provided at all or not of type list')
        if not isinstance(menu, dict):
            raise PyBarException.InvalidInputException('Menu was provided is of a foreign type: expected dictionary')
        # if table_list == [] or groups_list == [] or workers_list == []:
        # raise PyBarException.InvalidInputException('One list or more is empty!')
        self.shift_number = shift_number
        self.table_list = deepcopy(table_list)
        self.groups_list = deepcopy(groups_list)
        self.workers_list = deepcopy(workers_list)
        self.menu = menu
        self.__total_money = 0
        self.__total_tip = 0

    def __repr__(self):
        return self.shift_number

    def __str__(self):
        return f'Shift number {self.shift_number}'

    def add_money(self, money):
        if money < 0:
            raise PyBarException.InvalidInputException('Can not subtract money from the cash register!')
        self.__total_money += money

    def add_tip(self, tip):
        if tip < 0:
            raise PyBarException.InvalidInputException('Can not subtract money from the cash register!')
        self.__total_tip += tip

    def get_money(self, manager):
        if not isinstance(manager, Manager):
            raise PyBarException.AccessDeniedException('Only a manager can access the money')
        return self.__total_money

    def get_tip(self, manager):
        if not isinstance(manager, Manager):
            raise PyBarException.AccessDeniedException('Only a manager can access the tip')
        return self.__total_tip

    def shift_day(self):
        for worker in self.workers_list:
            worker.work(self)
            print('_'*40)

    def get_group_list(self):
        return deepcopy(self.groups_list)

