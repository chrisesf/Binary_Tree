class Node:
    def __init__(self, key, info, left = None, right = None):
        self.key = key
        self.info = info
        self.left = left
        self.right = right

    def insert(self, key, value):
        if key < self.key:
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.left.insert(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key, value)
            else:
                print(value)
                self.right.insert(key, value)
        else:
            return None

    def search(self, key):
        if key < self.key:
            if self.left is None:
                return None
            else:
                return self.left.search(key)
        elif key > self.key:
            if self.right is None:
                return None
            else:
                return self.right.search(key)
        else:
            return self.info

    def removeLeaf(self, key):
        if self.left and self.left.left is None and self.left.right is None and self.left.key == key:
            self.left = None
            return True
        if self.right and self.right.left is None and self.right.right is None and self.right.key == key:
            self.left = None
            return True
        if self.left and self.key > key:
            return self.left.removeLeaf(key)
        if self.right and self.key < key:
            return self.right.removeLeaf(key)
        return False

    def removeSub(self, key):
        if self.left and self.left.left is None and self.left.right is None and self.left.key == key:
            if self.left.left:
                self.left = self.left.left
            if self.left.right:
                self.left = self.left.right
            return True
        if self.right and self.right.left is None and self.right.right is None and self.right.key == key:
            self.right = self.right.right
            return True
        if self.left and self.key > key:
            return self.left.removeLeaf(key)
        if self.right and self.key < key:
            return self.right.removeLeaf(key)
        return False

tree = Node(535, "A")
tree.insert(23, "B")
tree.insert(11, "C")
tree.insert(88, "D")

print(tree.search(11))

print(tree.removeLeaf(11))

print(tree.search(11))
