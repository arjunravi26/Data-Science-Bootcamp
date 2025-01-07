class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return

    def delete(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        curr = self.head
        while curr:
            if curr.next.value == value:
                curr.next = curr.next.next
                return True
            curr = curr.next
        return False

    def traverse(self):
        if not self.head:
            return False
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next


linked_list = Linkedlist()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(39)
linked_list.traverse()
linked_list.delete(39)
linked_list.traverse()
