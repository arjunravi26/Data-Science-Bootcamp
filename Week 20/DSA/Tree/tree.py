class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return True
        self._insert(self.root, value)

    def _insert(self, node, value):
        queue = [node]
        while queue:
            curr = queue.pop(0)
            if curr.left:
                queue.append(curr.left)
            else:
                print("Inserting in left node")
                curr.left = Node(value)
                return True
            if curr.right:
                queue.append(curr.right)
            else:
                print("Inserting in right node")
                curr.right = Node(value)
                return True

    def delete(self,value):
        if not self.root:
            return False
        queue = [self.root]
        node_delete = None
        while queue:
            curr = queue.pop(0)
            if curr.value == value:
                node_delete = curr
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        node_delete.value = curr.value
        self._delete_last(curr)
    def _delete_last(self, node):
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if curr.left == node:
                curr.left = None
                return True
            if curr.left:
                queue.append(curr.left)
            if curr.right == node:
                curr.right = None
                return True
            if curr.right:
                queue.append(curr.right)
            
    def search(self, value):
        pass

    def inorder(self):
        if self.root is None:
            return False
        self._inorder(self.root)

    def _inorder(self, node):
        if not node:
            return None
        self._inorder(node.left)
        print(node.value)
        self._inorder(node.right)

    def preorder(self):
        pass

    def postorder(self):
        pass


tree = Tree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(101)
tree.insert(201)
tree.insert(302)
tree.inorder()
tree.delete(101)
tree.delete(302)
print("Tree after deletion")
tree.inorder()
