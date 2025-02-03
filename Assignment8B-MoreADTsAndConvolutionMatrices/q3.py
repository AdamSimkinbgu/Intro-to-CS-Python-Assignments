import random

lambda_list = []
for _ in range(63):
    k = random.randint(2, 100)
    lambda_list.append(lambda x: x % k == 0)

def printree(t, bykey=True):
    """Print a textual representation of t
    bykey=True: show keys instead of values"""
    # for row in trepr(t, bykey):
    #        print(row)
    return trepr(t, bykey)


def trepr(t, bykey=False):
    """Return a list of textual representations of the levels in t
    bykey=True: show keys instead of values"""
    if t == None:
        return ["#"]

    thistr = str(t.key) if bykey else str(t.val)  # + ": " + str(t.val)

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))


def conc(left, root, right):
    """Return a concatenation of textual represantations of
    a root node, its left node, and its right node
    root is a string, and left and right are lists of strings"""

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result


def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1


def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i


###################################### ---Q3A--- ######################################
class BinaryDecisionTreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.right = None
        self.left = None

    def __repr__(self):
        return f'{self.key}: {self.val}'

    def is_leaf(self):
        """
        A query to test if a node is a leaf.
        :return [bool] for if is leaf.
        """
        if self.right != None or self.left != None:
            return False
        return True

###################################### ---Q3B--- ######################################
class BinaryDecisionTree:
    def __init__(self, elements: list):
        """ A loop creating a list out of the given elements while morphing them into tree nodes. """
        index = 0
        for elem in elements:
            elements[index] = BinaryDecisionTreeNode(index, elem)
            index += 1

        self.decision_tree_root = elements[0]


        def wrapper(array, i=0):
            """
            A wrapper that builds the tree recursively, linking nodes to their respective
            leads.
            :param array [list] - The nodes to build the tree from in a list.
            :param i [int] - The index of the current node, linking it to its leads.
            :return None. The function changes inplace leads to nodes.
            """
            if (2 * i + 1) >= len(array):
                return

            if (2 * i + 2) >= len(array):
                array[i].left = array[2 * i + 1]
                return

            array[i].left = array[2 * i + 1]
            array[i].right = array[2 * i + 2]
            wrapper(array, i + 1)

        wrapper(elements)

    def __repr__(self):
        # no need to understand the implementation of this one
        out = ""
        # need printree.py file or make sure to run it in the NB
        for row in printree(self.decision_tree_root):
            out = out + row + "\n"
        return out

    ###################################### ---Q3C--- ######################################
    def decide(self, input_value):
        """
        This function is given an input that the whole tree can accept, the returns the route it takes down the tree
        to the last node he encounters, the leaf.
        :param input_value [acceptable input] - Acceptable input is one that all nodes can calculate.
        :return [str] - A string showing the path, for example: 0->1->3 - starting in 0, passing 1 and ending in 3.
                        The numbers represent the keys traveled through.
        """

        def wrapper(curr, string, subject):
            """
            A recursive method that creates the asked string.
            :param curr [BinaryDecisionTreeNode] - The current tree node looked at.
            :param string [str.. da..] - The string created in the process.
            :param subject [input_value] - The initial input to the @decide function.
            :return [str] - A string showing the path, for example: 0->1->3 - starting in 0, passing 1 and ending in 3.
                            The numbers represent the keys traveled through.
            """
            if curr.is_leaf():
                string += str(curr.key)
                return string
            if curr.val(subject):
                string += str(curr.key) + '->' + wrapper(curr.left, string, subject)
            else:
                string += str(curr.key) + '->' + wrapper(curr.right, string, subject)

            return string

        return wrapper(self.decision_tree_root, '', input_value)

        # def wrapper(wrapper_val: BinaryDecisionTreeNode, initial_input, string):
        #     string += str(wrapper_val.key)
        #     if not wrapper_val.is_leaf():
        #         if wrapper_val.val(initial_input):
        #             print(f'after going left {string}')
        #             wrapper(wrapper_val.left, initial_input, string)
        #         else:
        #             print(f'after going right {string}')
        #             wrapper(wrapper_val.right, initial_input, string)
        #             return string
        #     print(f'ending {string}')
        #     return string
        #
        # if self.decision_tree_root.val(input_value):
        #     init_string += str(self.decision_tree_root.key)
        #     if self.decision_tree_root.left:
        #         return wrapper(self.decision_tree_root.left, input_value, init_string)
        #
        # init_string += str(self.decision_tree_root.key)
        # if self.decision_tree_root.right:
        #     return wrapper(self.decision_tree_root.right, input_value, init_string)


    ###################################### ---Q3D--- ######################################
    def output(self, input_value):
        """
        A function that takes the leaf that a given input ends in and returns the calculated value for a non-binary
        function. If the function for the leaf node is binary, return None.
        :param input_value [any input] - Any input that would be able to be calculated in the tree nodes.
        :return The output of the non-binary function in the tree node.
        """
        leaf_to_test = BinaryDecisionTree.decide(self, input_value).split('->')[-1]

        def rec_search(curr, some_input, some_func):
            """
            A recursive search for the value in the leaf.
            :param curr [BinaryDecisionTreeNode] - The current node in question.
            :param some_input [acceptable input] - Acceptable input is one that all nodes can calculate.
            :param some_func [lambda] - The function at the leaf. Initially an empty string.
            :return [lambda] - The function at the respective leaf.
            """
            if some_input == str(curr.key):
                some_func = curr.val
                return some_func
            if some_input > str(curr.key):
                if curr.left != None:
                    some_func = rec_search(curr.left, some_input, some_func)
                if curr.right != None:
                    some_func = rec_search(curr.right, some_input, some_func)
            return some_func

        lambda_to_use = rec_search(self.decision_tree_root, leaf_to_test, "")
        res = lambda_to_use(input_value)
        # if res == False or res == None:
        #     return None
        if isinstance(res, bool) or res == None:
            return None
        return res


    ###################################### ---Q3E--- ######################################
    def compact(self):
        """
        This method creates a list of list containing all the functions in each level. Each level is in a different
        list index in the main list. Each function, from left to right, is the first of any level of the tree.
        For example: [ (main list) [ (height 0) ], [ (height 1) ], [ (height 2) ], ... , [ (height h - 1) ], [ (height h) ] ]
        :return [list[lists]] - The list of all nodes values orders as mentioned above.
        """
        def wrapper(curr, h=0):
            """
            A quick check of height. Only need to check left most lead because the tree is ordered and partially to
            fully filled.
            :param curr [BinaryDecisionTreeNode] - The current tree node in question.
            :param h [int] - Initialized to 0. Saves the height reached.
            :return [int] , the height reached.
            """
            if curr.left:
                return wrapper(curr.left, h + 1)
            return h
        height = wrapper(self.decision_tree_root)

        levels_list = [[] for _ in range(height + 1)]

        def wrapper2(curr: BinaryDecisionTreeNode, h=0):
            """
            This method inserts the values of all the nodes of the tree in their respective location in the lists.
            :param curr [BinaryDecisionTreeNode] - The current tree node in question.
            :param h [int] - Initialized to 0. The current height the function is operating on.
            :return None. The function makes inplace changes of the list.
            """
            levels_list[h].append(curr.val)
            if curr.is_leaf():
                return
            if curr.left != None:
                wrapper2(curr.left, h + 1)
            if curr.right != None:
                wrapper2(curr.right, h + 1)

        wrapper2(self.decision_tree_root)
        return levels_list

        # def height(root):
        #     if root is None:
        #         return 0
        #     left_height = height(root.left)
        #     right_height = height(root.right)
        #     return max(left_height, right_height) + 1
        #
        # height = height(self.decision_tree_root) - 1

        # for first in range(height):
        #     levels_list[first] = 'hey'





