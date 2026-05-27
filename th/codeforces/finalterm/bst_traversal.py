import sys
import collections
write = sys.stdout.write

class Node():
    __slots__ = ['data', 'left', 'right']
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BSTTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        self.__insertNode(self.root, data)
    
    def __insertNode(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.__insertNode(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.__insertNode(node.right, data)

    def search(self, data):
        if self.root is None:
            write("false\n")
            return
        self.__searchNode(self.root, data)

    def __searchNode(self, node, data):
        if node is None:
            write("false\n")
            return
        
        if node.data > data:
            self.__searchNode(node.left, data)
        elif node.data < data:
            self.__searchNode(node.right, data)
        else:
            write("true\n")
            return

    def delete(self, data):
        self.root, deleted = self.__deleteNode(self.root, data)
        if deleted:
            write("true\n")
        else:
            write("false\n")

    def __deleteNode(self, node, data):
        if node is None:
            return None, False
        if data < node.data:
            node.left, deleted = self.__deleteNode(node.left, data)
            return node, deleted
        elif data > node.data:
            node.right, deleted = self.__deleteNode(node.right, data)
            return node, deleted
        else:
            # One child
            if node.left is None:
                return node.right, True
            if node.right is None:
                return node.left, True
            # Two children
            succ = node.right
            while succ.left is not None:
                succ = succ.left
            node.data = succ.data
            node.right, _ = self.__deleteNode(node.right, succ.data)
            return node, True

    def preOrderTraversal(self):
        if self.root is None:
            write("\n")
            return
        treeTraversal = []
        self.__preOrderTraversal(self.root, treeTraversal)
        write(f"{' '.join(str(value) for value in treeTraversal)}\n")

    def __preOrderTraversal(self, node, treeTraversal):
        if node is None:
            return
        treeTraversal.append(node.data)
        self.__preOrderTraversal(node.left, treeTraversal)
        self.__preOrderTraversal(node.right, treeTraversal)

    def inOrderTraversal(self):
        if self.root is None:
            write("\n")
            return
        treeTraversal = []
        self.__inOrderTraversal(self.root, treeTraversal)
        write(f"{' '.join(str(value) for value in treeTraversal)}\n")

    def __inOrderTraversal(self, node, treeTraversal):
        if node is None:
            return
        self.__inOrderTraversal(node.left, treeTraversal)
        treeTraversal.append(node.data)
        self.__inOrderTraversal(node.right, treeTraversal)

    def postOrderTraversal(self):
        if self.root is None:
            write("\n")
            return
        treeTraversal = []
        self.__postOrderTraversal(self.root, treeTraversal)
        write(f"{' '.join(str(value) for value in treeTraversal)}\n")

    def __postOrderTraversal(self, node, treeTraversal):
        if node is None:
            return
        self.__postOrderTraversal(node.left, treeTraversal)
        self.__postOrderTraversal(node.right, treeTraversal)
        treeTraversal.append(node.data)

    def LevelOrder(self):
        treeTraversal = []
        q = collections.deque()
        q.append(self.root)
        while q:
            top = q.popleft()
            treeTraversal.append(top.data)
            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)
        write(f"{' '.join(str(value) for value in treeTraversal)}\n")

def main():
    input_data = sys.stdin.read().strip()
    iterator = iter(input_data.split())

    tree = BSTTree()
    for cmd in iterator:
        if cmd == '1':
            value = int(next(iterator))
            tree.insert(value)
        elif cmd == '3':
            traversalType = next(iterator)
            if traversalType == 'NLR':
                tree.preOrderTraversal()
            elif traversalType == 'LNR':
                tree.inOrderTraversal()
            elif traversalType == 'LRN':
                tree.postOrderTraversal()
            elif traversalType == 'LevelOrder':
                tree.LevelOrder()
        elif cmd == '4':
            value = int(next(iterator))
            tree.search(value)
        elif cmd == '2':
            value = int(next(iterator))
            tree.delete(value)

if __name__ == "__main__":
    main()