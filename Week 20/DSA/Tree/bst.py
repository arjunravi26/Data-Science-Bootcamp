class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self,value):
        if not self.root:
            self.root = Node(value)
            return
        self._insert(self.root,value)
    def _insert(self,node,value):
        if node.value < value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left,value)
        elif node.value > value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right,value)
        else:
            print(f"{value} is already present in the tree")

    def delete(self):
        pass
    def search(self,value):
        pass
    def inorder(self):
        if not self.root:
            print("BST is empty")
        self._inorder(self.root)
    def _inorder(self,node):
        if not node:
            return
        self._inorder(node.left)
        print(node.value)
        self._inorder(node.right)

tree = BST()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(5)
tree.insert(8)
tree.inorder()