class StackOverflow(Exception):
    pass


class StackUnderflow(Exception):
    pass


class Queue:
    def __init__(self, size) -> None:
        self.queue = []
        self.size = size
        self.length = 0

    def insert(self, value):
        if self.isFull():
            return StackOverflow("Stack Overflow error")
        self.queue.append(value)
        self.length += 1

    def delete(self):
        if self.isEmpty():
            raise StackUnderflow("Stack Undeflow error")
        self.queue.pop(0)
        self.length -= 1

    def isFull(self):
        return self.length == self.size

    def isEmpty(self):
        return self.length == 0

    def print_queue(self):
        print(self.queue)


queue = Queue(5)
queue.insert(10)
queue.insert(20)
queue.insert(30)
queue.insert(40)
queue.insert(50)
queue.print_queue()
queue.delete()
queue.delete()
queue.insert(60)
queue.print_queue()
