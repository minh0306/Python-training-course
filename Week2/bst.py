# A Python script (bst.py) with a BinarySearchTree class, supporting insertion and search. (Optional)
class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, key: int):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    def _insert(self, root: Node, key: int):
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        elif key > root.key:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root  
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.key)
            self._inorder(root.right, result)


bst = BinarySearchTree()
for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
    bst.insert(value)

print("In-order traversal:", bst.inorder())  # [1, 3, 4, 6, 7, 8, 10, 13, 14]

found = bst.search(7)
print("Search 7:", "Found" if found else "Not Found")

not_found = bst.search(2)
print("Search 2:", "Found" if not_found else "Not Found")