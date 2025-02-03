class Node:
    def __init__(self, data):
        """
        constructor, that builds up one node
        :param data: the specific data to hold on the node value
        """
        self.value = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.value)


class DoublyLinkedList:
    def __init__(self):
        """
        initializing the DoublyLinkedList
        """
        self.head = None
        self.tail = None
        self.len = 0

    def __repr__(self):
        out = ""
        p = self.head
        while p is not None:
            if p.next != None:
                out += str(p) + " " + "->"
            else:
                out += str(p) + " "
            p = p.next
        return out

    # Define the push method to add elements at the beginning
    def push(self, new_val):
        new_node = Node(new_val)
        new_node.prev = None
        new_node.next = self.head
        if self.len == 0:
            self.head = new_node
            self.tail = new_node
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        self.len += 1

    # Define the append method to add elements at the end
    def append(self, new_val):
        new_node = Node(new_val)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
            self.len += 1
            return
        last = self.tail
        while last.next is not None:
            # self.len += 1
            last = last.next
        last.next = new_node
        new_node.prev = last
        self.tail = new_node
        self.len += 1
        return

    def __len__(self):
        ''' called when using Python's len() '''
        return self.len

    def __getitem__(self, loc):
        ''' called when using L[i] for reading
            return node at location 0<=loc<len '''
        p = self.head
        for i in range(0, loc):
            p = p.next
        return p

    def __setitem__(self, loc, val):
        ''' called when using L[loc]=val for writing
            assigns val to node at location 0<=loc<len '''
        p = self.head
        for i in range(0, loc):
            p = p.next
        p.value = val
        return None

    def delete(self, loc):
        ''' delete element at location 0<=loc<len '''
        if loc == 0:
            self.head = self.head.next
        else:
            p = self.head
            for i in range(1, loc):
                p = p.next
            if p.next != None:  # p cannot be None
                p.next = p.next.next
        self.len -= 1

    def __iter__(self):
        self.runner = self.head
        return self

    def __next__(self):
        if self.runner is None:
            raise StopIteration
        res = self.runner
        self.runner = self.runner.next
        return res

    def __str__(self):
        out = ""
        p = self.head
        while p is not None:
            if p.next != None:
                out += str(p)
            else:
                out += str(p)
            p = p.next
        return out  # + "None"

