class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, value):
        if not self.head:
            self.head = Node(value)
            return True
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)
        return True

    def delete(self, value):
        if not self.head:
            return False
        curr = self.head
        if curr.value == value:
            self.head = self.head.next
            return True
        while curr.next:
            if curr.next.value == value:
                curr.next = curr.next.next
                return True
            curr = curr.next
        print(f"{value} does not exist in the linked list")

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        self.traverse()

    def traverse(self):
        if not self.head:
            return None
        curr = self.head
        print('Traverse into the list:')
        while curr:
            print(curr.value, end="," if curr.next else "\n")
            curr = curr.next

    def print_list(self, node):
        if not node:
            return None
        curr = node
        print('Traverse into the list:')
        while curr:
            print(curr.value, end="," if curr.next else "\n")
            curr = curr.next

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.value

    def delete_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next

    def split_half(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        first_half = self.head
        prev.next = None
        second_half = slow
        self.print_list(first_half)
        self.print_list(second_half)
        return first_half, second_half


ll = LinkedList()
ll.insert(20)
ll.insert(10)
ll.insert(15)
ll.insert(20)
ll.insert(10)
ll.insert(15)
ll.traverse()
print(ll.find_middle())
ll.delete(15)
# ll.delete(15)
ll.delete(9)
ll.traverse()
print(ll.detect_cycle())
ll.traverse()
ll.reverse()
ll.delete_middle()
ll.split_half()
