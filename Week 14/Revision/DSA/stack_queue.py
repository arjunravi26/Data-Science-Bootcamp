from collections import deque


# Implementing stack using queue
class Stack:
    def __init__(self) -> None:
        self.q1 = deque()
        self.q2 = deque()

    def push(self, value):
        self.q1.append(value)

    def pop(self):
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        value = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return value

    def print_stack(self):
        print("Stack values are:")
        print(self.q1)


stack = Stack()
stack.push(10)
stack.push(30)
stack.push(20)
stack.push(40)
stack.print_stack()
stack.pop()
stack.print_stack()
