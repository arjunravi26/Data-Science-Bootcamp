class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        self._insert(self.root, value)

    def _insert(self, node, value):
        if node.value > value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif node.value < value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
        else:
            print(f"{value} is already present in the tree")
            return

    def delete(self, value):
        if not self.root:
            return False
        self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return False
        if node.value > value:
            node.left = self._delete(node.left, value)
        elif node.value < value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self.find_min(node)
                node.value = min_node.value
                node.right = self._delete(node.right, min_node.value)
        return node

    def search(self, value):
        if not self.root:
            return None
        node = self.root
        while node:
            if node.value == value:
                return node.value
            elif node.value > value:
                node = node.left
            else:
                node = node.right
        return None

    def find_min(self, node):
        if node.left is None:
            return node
        return self.find_min(node.left)

    def inorder(self):
        if not self.root:
            print("BST is empty")
            return
        print("Inorder Traversal")
        self._inorder(self.root)

    def _inorder(self, node):
        if not node:
            return
        self._inorder(node.left)
        print(node.value)
        self._inorder(node.right)

    def preorder(self):
        if not self.root:
            print("BST is empty")
            return
        print("Pre order Traversal")
        self._preorder(self.root)

    def _preorder(self, node):
        if not node:
            return False
        print(node.value)
        self._preorder(node.left)
        self._preorder(node.right)

    def postorder(self):
        if not self.root:
            print("BST is empty")
            return
        print("Post order Traversal")
        self._postorder(self.root)

    def _postorder(self, node):
        if not node:
            return
        self._postorder(node.left)
        self._postorder(node.right)
        print(node.value)

    def find_height(self,node):
        if not self.root:
            return -1
        left = self.find_height(node.left)
        right = self.find_height(node.right)
        return 1 + max(left,right)


    def find_depth(self, value):
        if not self.root:
            return -1
        return self._depth(self.root, value, 0)

    def _depth(self, node, value, depth=0):
        if node is None:
            return -1
        if node.value == value:
            return depth
        if node.value > value:
            return self._depth(node.left, value, depth+1)
        elif node.value < value:
            return self._depth(node.right, value, depth+1)


tree = BST()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(12)
tree.insert(5)
tree.insert(8)
tree.inorder()
tree.preorder()
tree.postorder()
tree.delete(30)
tree.postorder()
print(tree.search(5))
print(tree.find_height(20))
print(tree.find_depth(8))
