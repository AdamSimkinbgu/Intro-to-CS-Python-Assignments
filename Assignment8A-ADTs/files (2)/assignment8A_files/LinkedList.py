class Node:
    def __init__(self, val):
        """
            constructor, that builds up one node
            :param val: the specific val to hold on the node value
        """
        self.value = val
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def add_at_start(self, val):
        """ add node with value val at the list head """
        new_node = Node(val)
        if self.len == 0:
            self.head = new_node
        else:
            tmp = self.head
            self.head = new_node
            self.head.next = tmp
        self.len += 1

    def insert(self, loc, val):
        """ add node with value val at location 0<=loc<len of the list """
        new_node = Node(val)
        if loc == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            p = self.head
            for i in range(1, loc):
                p = p.next
            tmp = p.next
            p.next = new_node
            p.next.next = tmp
        self.len += 1

    def delete(self, loc):
        """ delete element at location 0<=loc<len """
        if loc == 0:
            self.head = self.head.next
        else:
            p = self.head
            for i in range(1, loc):
                p = p.next
            if p.next is not None:  # p cannot be None
                p.next = p.next.next
        self.len -= 1

    def add_at_end(self, val):
        """ add node with value val at the list tail """
        new_node = Node(val)
        if self.len == 0:
            self.head = new_node
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = new_node
        self.len += 1

    def __len__(self):
        """ called when using Python's len() """
        return self.len

    def __getitem__(self, loc):
        """ called when using L[i] for reading
            return node at location 0<=loc<len """
        p = self.head
        for i in range(0, loc):
            p = p.next
        return p

    def __setitem__(self, loc, val):
        """ called when using L[loc]=val for writing
            assigns val to node at location 0<=loc<len """
        p = self.head
        for i in range(0, loc):
            p = p.next
        p.value = val
        return None

    def __repr__(self):
        out = ""
        p = self.head
        while p is not None:
            if p.next is not None:
                out += str(p) + " " + "->"
            else:
                out += str(p) + " "
            p = p.next

        return out  # + "None"

    def __str__(self):
        out = ""
        p = self.head
        while p is not None:
            if p.next != None:
                out += str(p)
            else:
                out += str(p)
            p = p.next
        return out 

    def __iter__(self):
        self.runner = self.head
        return self

    def __next__(self):
        if self.runner is None:
            raise StopIteration
        res = self.runner
        self.runner = self.runner.next
        return res
