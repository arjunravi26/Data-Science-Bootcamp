class Queue:
    def __init__(self, size) -> None:
        self.size = size
        self.queue = []
        self.length = 0

    def insert_front(self, value):
        if self.isFull():
            print("Stack Overflow")
            return False
        self.queue.insert(0, value)
        self.length += 1
        return True

    def insert_rear(self, value):
        if self.isFull():
            print("Stack Overflow")
            return False
        self.queue.append(value)
        self.length += 1

    def delete_rear(self):
        if self.isEmpty():
            print("Stack Underflow")
            return False
        self.queue.pop()
        self.length -= 1

    def delete_front(self):
        if self.isEmpty():
            print("Stack Underflow")
            return False
        self.queue.pop(0)
        self.length -= 1

    def isFull(self):
        return self.length == self.size

    def isEmpty(self):
        return self.length == 0

    def print_queue(self):
        print(self.queue)


dq = Queue(5)
dq.insert_front(10)
dq.insert_front(20)
dq.insert_rear(90)
dq.insert_rear(56)
dq.insert_front(1)
dq.print_queue()
dq.delete_front()
dq.print_queue()
dq.delete_rear()
dq.print_queue()