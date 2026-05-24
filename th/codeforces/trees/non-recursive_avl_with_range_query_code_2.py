import sys

class Node():
    __slots__ = ['data', 'height', 'size', 'left', 'right']
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.size = 1
        self.left = None
        self.right = None

class AVLTree():
    def __init__(self):
        self.root = None

    def update(self, node):
        lh = node.left.height if node.left else 0
        rh = node.right.height if node.right else 0
        node.height = 1 + (lh if lh > rh else rh)

        ls = node.left.size if node.left else 0
        rs = node.right.size if node.right else 0
        node.size = 1 + ls + rs
    
    def right_rotate(self, parent):
        child = parent.left
        parent.left = child.right
        child.right = parent

        self.update(parent)
        self.update(child)

        return child

    def left_rotate(self, parent):
        child = parent.right
        parent.right = child.left
        child.left = parent

        self.update(parent)
        self.update(child)

        return child
    
    def getBalance(self, node):
        lh = node.left.height if node.left else 0
        rh = node.right.height if node.right else 0
        return rh - lh

    def rebalance(self, node):
        self.update(node)
        bal = self.getBalance(node)

        if bal < -1:
            if self.getBalance(node.left) <= 0:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
        
        if bal > 1:
            if self.getBalance(node.right) >= 0:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
            
        self.update(node)

        return node

    
    def insert(self, data, node = None):
        if node is None:
            return Node(data)

        if node.data > data:
            node.left = self.insert(data, node.left)
        elif node.data < data:
            node.right = self.insert(data, node.right)
        else:
            return node
        
        return self.rebalance(node)
    
    def delete(self, data, node = None):
        if node is None:
            return None
        
        if node.data > data:
            node.left = self.delete(data, node.left)
        elif node.data < data:
            node.right = self.delete(data, node.right)
        else:
            # Current node has 0 or 1 children
            if not node.left or not node.right:
                return node.left if node.left else node.right
            else:
                # Find min value of node in right branch
                curr = node.right
                while curr.left is not None:
                    curr = curr.left
                
                node.data = curr.data
                node.right = self.delete(curr.data, node.right)
            
        return self.rebalance(node)
            
    def queryRange(self, x, y):
        if x > y:
            x, y = y, x
        count = 0
        curr = self.root
        while curr:
            if curr.data > y:
                curr = curr.left
            elif curr.data < x:
                count = count + (curr.left.size if curr.left else 0) + 1
                curr = curr.right
            else:
                count = count + (curr.left.size if curr.left else 0)
                return count
        return -1

    def preOrderTraversal(self):
        stack = [self.root] if self.root else []
        result = []
        while stack:
            curr = stack.pop()
            result.append(str(curr.data))
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return ' '.join(result)
    

def main():
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)
    tree = AVLTree()
    for cmd in iterator:
        t = int(cmd)
        if t == 1:
            x = int(next(iterator))
            tree.root = tree.insert(x, tree.root)
        elif t == 2:
            x = int(next(iterator))
            tree.root = tree.delete(x, tree.root)
        elif t == 3:
            x, y = int(next(iterator)), int(next(iterator))
            print(tree.queryRange(x, y))
        else:
            print(tree.preOrderTraversal())

if __name__ == "__main__":
    main()
    