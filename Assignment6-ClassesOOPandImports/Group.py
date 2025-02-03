import PyBarException
from copy import deepcopy


class Group:
    def __init__(self, customer_list, order_dict):
        if not isinstance(customer_list, list):
            raise PyBarException.InvalidInputException("The group must be a list of customers")
        if len(customer_list) < 2:
            raise PyBarException.InvalidInputException("Can't be less then 2")
        self.customer_list = deepcopy(customer_list)
        self.__order_dict = order_dict

    def __repr__(self):
        return self.customer_list, self.__order_dict

    def __str__(self):
        return f'The Group has {len(self.customer_list)} members, their order: {self.__order_dict}'

    def __lt__(self, other):
        if not isinstance(other, Group):
            raise PyBarException.InvalidInputException('A groups can only be compared to another group')
        return len(self.customer_list) < len(other)

    def __len__(self):
        return len(self.customer_list)

    def get_order(self):
        return deepcopy(self.__order_dict)

    def get_customers_string(self):
        name_list = [customer.get_name() for customer in self.customer_list]
        return_string = ", ".join(name_list[:-1]) + " and " + name_list[-1]
        return return_string

# group1 = Group([Customer('adam', 19), Customer('ella', 24), Customer("Neta", 20, 0.12), Customer("Avi", 20, 0.12)], {"Negev": 3, "Coke":2, "Pizza": 2})
# print(group1.get_customers_string())
# print(group1.customer_list[0].get_name())
# group2 = Group([Customer('noa', 23)], {"Negev": 3, "Coke":2, "Pizza": 2})