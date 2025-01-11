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

    def find_middle(self):
        if not self.head:
            return False
        print()
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

    def delete_mid(self):
        if not self.head:
            return False
        print()
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next

    def split(self):
        if not self.head:
            return False
        print()
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        lst2 = slow.next
        slow.next = None
        lst1 = self.head
        while lst1.next:
            print(lst1.data,end=",")
            lst1 = lst1.next
        print(lst1.data)
        while lst2.next:
            print(lst2.data,end=",")
            lst2 = lst2.next
        print(lst2.data)

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
dll.insert(100)
dll.insert(308)
dll.insert(4)
dll.traverse()
# dll.delete(10)
dll.traverse()
dll.find_middle()
# dll.delete_mid()
dll.traverse()
dll.split()