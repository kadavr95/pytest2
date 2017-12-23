class Stack(list):
    """Stack represenation."""
    def push(self, value):
        self.append(value)
    def __str__(self):
        return "Stack::{0}".format(self)