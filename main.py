class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def search(self, key):
        pass

    def insert(self, key):
        pass

    def fix_insert(self, k):
        pass

    def print_tree_height(self):
        pass

    def print_black_height(self):
        pass

    def print_tree_size(self):
        pass
