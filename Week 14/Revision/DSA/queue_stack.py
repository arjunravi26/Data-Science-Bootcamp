class Queue:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []

    def enqueue(self, value):
        self.s1.append(value)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def print_queue(self):
        print(self.s1, self.s2)


queue = Queue()
queue.enqueue(10)
queue.enqueue(30)
queue.enqueue(20)
queue.enqueue(40)
queue.print_queue()
queue.dequeue()
queue.print_queue()
queue.dequeue()
queue.print_queue()