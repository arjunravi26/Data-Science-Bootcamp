class StackUnderflowError(Exception):
    pass


class StackOverflowError(Exception):
    pass


class Stack:
    def __init__(self, size) -> None:
        self.size = size
        self.stack = []
        self.length = 0

    def insert(self, value):
        if not self.isFull():
            self.stack.append(value)
            stack.length += 1
            return True
        else:
            raise StackOverflowError("StackOverflow")

    def delete(self):
        if not self.isEmpty():
            del_value = self.stack.pop()
            self.length -= 1
            return del_value
        raise StackUnderflowError("StackUnderflow")

    def isFull(self):
        if self.length == self.size:
            return True
        return False

    def isEmpty(self):
        if self.length == 0:
            return True
        return False

    def print_stack(self):
        print(self.stack)


stack = Stack(5)
stack.insert(10)
stack.insert(20)
stack.insert(30)
stack.insert(40)
stack.insert(50)
# stack.insert(60)
stack.delete()
stack.insert(60)
stack.print_stack()
