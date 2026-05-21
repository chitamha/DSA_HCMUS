import sys

write = sys.stdout.write

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left_positive_sum = value if value >= 0 else 0
        self.len = 1 if value >= 0 else 0

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if node.right is None:
            node.right = Node(value)
        else:
            self._insert_recursive(node.right, value)
            if node.right.len == 0:
                node.left_positive_sum = node.right.left_positive_sum
                node.len = node.right.len
            else:


            tmp_sum = node.left_positive_sum + node.right.left_positive_sum
            node.left_positive_sum = 



    def delete(self):
        if self.root is not None:
            self._delete_recursive(self.root)
    
    def _delete_recursive(self, node):
        if node.left is not None:
            self._delete_recursive(node.left)
        else:
            node = None
        
    
