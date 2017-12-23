class Stack(object):
    """Stack represenation."""
    def __init__(self):
           self._stack = []
    def push(self, value):
           self._stack.append(value)
    def pop(self):
            return self._stack.pop()
    def length(self):
            return len(self._stack)
    def __add__(self, other):
            s = Stack()
            s._stack = self._stack[:] + other._stack[:]
            return s
    def __str__(self):
        return "Stack::{0}".format(self._stack)