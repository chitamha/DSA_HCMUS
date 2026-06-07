import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class Tree:
    def __init__(self, node = None):
        self.root = node

    def traverse(self, node):
        if node is not None:
            self.traverse(node.left)
            print(node.value)
            self.traverse(node.right)

    def kthElement(self, node, value):
        pass

    def replaceRecursive(self, node):
        if node is not None:
            node.left = self.replaceRecursive(node.left)
            node.value = self.kthElement(self, node.value)
            node.right = self.replaceRecursive(node.right)
        return node

    def convertTree(self):
        self.root = self.replaceRecursive(self.root)

if __name__ == "__main__":
    root = Node(6);
    root.left = Node(5);
    root.right = Node(9);
    root.left.left = Node(2);
    root.left.right = Node(1);
    root.right.left = Node(10);
    root.right.right = Node(11);
    root.left.left.left = Node(12);
    root.left.left.right = Node(13);
    root.left.right.left = Node(0);
    root.left.right.right = Node(-1);

    tree = Tree(root);
    tree.convertTree();