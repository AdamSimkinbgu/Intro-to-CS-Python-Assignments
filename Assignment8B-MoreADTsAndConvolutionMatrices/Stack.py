
class Stack:
    def __init__(self):
        self.stack_vals = []
        self.len = 0

    def push(self, val):
        self.stack_vals.append(val)
        self.len += 1

    def pop(self):
        if self.is_empty():
            return None
        res = self.stack_vals[-1]
        self.stack_vals = self.stack_vals[0:-1]
        self.len -= 1
        return res

    def __repr__(self):
        out = '|'
        for i in range(self.len):
            out += str(self.stack_vals[i]) + ' '
        out += '<-top'
        return out

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_vals[-1]

    def __len__(self):
        return self.len

    def is_empty(self):
        return self.len == 0

