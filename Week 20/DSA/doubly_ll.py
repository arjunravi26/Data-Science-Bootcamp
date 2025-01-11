class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.head.prev = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def delete(self, value):
        if not self.head:
            return False
        curr = self.head
        if self.head.data == value:
            self.head.next.prev = None
            self.head = self.head.next
            return
        while curr.next.next:
            if curr.next.data == value:
                curr.next.next.prev = curr
                curr.next = curr.next.next
                return
            curr = curr.next
        if curr.next.data == value:
            curr.next.prev = None
            curr.next = None

    def traverse(self):
        if not self.head:
            return False
        curr = self.head
        print()
        while curr.next:
            print(f"{curr.data}->", end="")
            curr = curr.next
        print(curr.data, end="")


dll = LinkedList()
dll.insert(10)
dll.insert(30)
dll.insert(50)
dll.insert(60)
dll.traverse()
dll.delete(10)
dll.traverse()