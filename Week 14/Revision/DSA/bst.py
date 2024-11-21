class Tree:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Tree(value)
            return True
        return self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = Tree(value)
                return True
            self._insert(node.left, value)
        elif value > node.value:
            if not node.right:
                node.right = Tree(value)

                return True
            self._insert(node.right, value)

        else:
            print(f"Value {value} already exist in the binary search tree")
            return False

    def delete(self, value):
        if not self.root:
            return False
        self.root = self._delete(self.root, value)
        return True

    def _delete(self, node, value):
        if not node:
            return node
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            temp = self.find_min(node.right)
            node.value = temp.value
            node.right = self._delete(node.right, temp.value)
        return node

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def height(self):
        pass

    def depth(self):
        pass

    def inorder(self):
        if self.root:
            self._inorder(self.root)
        else:
            print("BST is empty")

    def _inorder(self, node):
        if not node:
            return
        self._inorder(node.left)
        print(node.value)
        self._inorder(node.right)

    def preorder(self):
        if self.root:
            self._preorder(self.root)
        else:
            print("BST is empty")

    def _preorder(self, node):
        if not node:
            return
        print(node.value)
        self._preorder(node.left)
        self._preorder(node.right)

    def postorder(self):
        if self.root:
            self._postorder(self.root)
        else:
            print("BST is empty")

    def _postorder(self, node):
        if not node:
            return
        self._postorder(node.left)
        self._postorder(node.right)
        print(node.value)

    def depth(self, node, value):
        if node is None:
            return -1
        left = self.depth(node.left)
        if left == -1:
            return left
        return self.depth(node.right)
    def height(self,node):
        if node is None:
            return -1
        left = self.height(node.left)
        right = self.height(node.right)
        return max(left,right) + 1

bst = BST()
# bst.inorder()
values = [10, 20, 5, 39, 30, 50, 44]
for val in values:
    bst.insert(val)
# bst.inorder()
bst.delete(39)
bst.inorder()
bst.preorder()
bst.postorder()
