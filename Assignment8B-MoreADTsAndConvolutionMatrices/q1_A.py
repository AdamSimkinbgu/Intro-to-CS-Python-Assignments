###################################### ---Q1A--- ######################################
from copy import deepcopy

from DNA import DNA
from Stack import Stack


def sort_DNA_Stack(DNA_stack: Stack):
    """
    Using only the given stack of DNA and another stack created in the function, able to sort DNA strands by their
    length and if length is equal between any number of strands, compares them by their mass instead.
    :param DNA_stack [Stack] - The given stack of DNA.
    :return A stack representing the sorted DNA stack by size/mass as required by the assignment.
    """
    temp_stack = Stack()
    while True:
        temp_item = DNA_stack.pop()
        if temp_item == None:
            while not temp_stack.is_empty():
                temp_item = temp_stack.pop()
                if temp_stack.is_empty():
                    DNA_stack.push(temp_item)
                    break
                if len(temp_item) == len(temp_stack.peek()):
                    if DNA.calculate_mass(temp_item) >= DNA.calculate_mass(temp_stack.peek()):
                        DNA_stack.push(temp_stack.pop())
                    DNA_stack.push(temp_item)
                else:
                    DNA_stack.push(temp_item)
            return DNA_stack
        temp_item_used = False
        while not temp_item_used:

            if temp_stack.is_empty():
                temp_stack.push(temp_item)
                temp_item_used = True
            elif len(temp_item) == len(temp_stack.peek()):
                if DNA.calculate_mass(temp_item) <= DNA.calculate_mass(temp_stack.peek()):
                    temp_stack.push(temp_item)
                    temp_item_used = True
                else:
                    DNA_stack.push(temp_stack.pop())
            elif len(temp_item) < len(temp_stack.peek()):
                temp_stack.push(temp_item)
                temp_item_used = True
            else:
                DNA_stack.push(temp_stack.pop())



