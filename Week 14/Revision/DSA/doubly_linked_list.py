class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_begin(self, value):
        if not self.head:
            self.head = Node(value)
            return True
        first = self.head
        self.head = Node(value)
        first.prev = self.head
        self.head.next = first
        return True

    def insert(self, value, pos):
        if pos == 1:
            self.insert_begin(value)
            return True
        current = self.head
        current_pos = 1
        while current:
            if current_pos == pos - 1:
                next = current.next
                current.next = Node(value)
                current.next.prev = current
                current.next.next = next
                return True
            current_pos += 1
            current = current.next
        if pos > current_pos:
            print(f"No such postion exist {pos}")
            return False

    def insert_end(self, value):
        if not self.head:
            self.head = Node(value)
            return False
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(value)
        curr.next.prev = curr

    def delete(self, value):
        if not self.head:
            return False
        curr = self.head
        if curr.value == value:
            self.head = self.head.next
            return True
        while curr.next:
            if curr.next.value == value:
                prev = curr
                curr.next = curr.next.next
                if curr.next:
                    curr.next.prev = prev
                return True
            curr = curr.next

    def traverse(self):
        if not self.head:
            return False
        curr = self.head
        print(f"Traverse list:\n")
        while curr:
            print(curr.value, end="," if curr.next else "\n")
            curr = curr.next

    def reverse(self):
        curr = self.head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            curr.prev = next
            prev = curr
            curr = next
        self.head = prev
        self.traverse()


dl = DoublyLinkedList()
dl.insert_begin(10)
dl.insert_begin(20)
dl.insert(100, 3)
dl.insert_end(89)
dl.insert_begin(50)
dl.insert_begin(60)
dl.traverse()
dl.delete(20)
dl.traverse()
dl.reverse()
