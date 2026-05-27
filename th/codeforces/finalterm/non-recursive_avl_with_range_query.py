import sys
write = sys.stdout.write

class Node:
    __slot__ = ['data', 'height', 'size', 'left', 'right']
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.size = 1
        self.left = None
        self.right = None

class AVL:
    def __init__(self):
        self.root = None

    def update(self, node):
        hleft = node.left.height if node.left else 0
        hright = node.right.height if node.right else 0
        node.height = 1 + (hleft if hleft >= hright else hright)

        sleft = node.left.size if node.left else 0
        sright = node.right.size if node.right else 0
        node.size = sleft + sright + 1

    def rightRotate(self, node):
        child = node.left
        node.left = child.right
        child.right = node
        self.update(node)
        self.update(child)
        return child
    
    def leftRotate(self, node):
        child = node.right
        node.right = child.left
        child.left = node
        self.update(node)
        self.update(child)
        return child
    
    def getbalance(self, node):
        hleft = node.left.height if node.left else 0
        hright = node.right.height if node.right else 0
        return hright - hleft
    
    def rebalance(self, node):
        self.update(node)
        bal = self.getbalance(node)
        # Lech trai
        if bal < -1:
            if self.getbalance(node.left) <= 0:
                node = self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                node = self.rightRotate(node)
        
        # Lech phai
        if bal > 1:
            if self.getbalance(node.right) >= 0:
                node = self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                node = self.leftRotate(node)

        return node
    
    def getMinValue(self, node):
        curr = node
        while curr.left:
            curr = curr.left
        return curr

    def insert(self, data):
        self.root = self.__insertRecursion(self.root, data)

    def __insertRecursion(self, node, data):
        if node is None:
            return Node(data)
        
        if data < node.data:
            node.left = self.__insertRecursion(node.left, data)
        elif data > node.data:
            node.right = self.__insertRecursion(node.right, data)

        return self.rebalance(node)
    
    def delete(self, data):
        self.root = self.__deleteRecursion(self.root, data)

    def __deleteRecursion(self, node, data):
        if node is None:
            return None
        
        if data < node.data:
            node.left = self.__deleteRecursion(node.left, data)
        elif data > node.data:
            node.right = self.__deleteRecursion(node.right, data)
        else:
            # Node co 0 hoac 1 con
            if not node.left or not node.right:
                temp = node.left if node.left else node.right
                return temp
            # Node co 2 con
            else:
                tmp = self.getMinValue(node.right)
                node.data = tmp.data
                node.right = self.__deleteRecursion(node.right, node.data)
        
        return self.rebalance(node)
                
    def getQuery(self, x, y):
        x, y = (y, x) if x > y else (x, y)

        ans, curr = 0, self.root
        while curr:
            if curr.data > y:
                curr = curr.left
            elif curr.data < x:
                ans += 1 + (curr.left.size if curr.left else 0)
                curr = curr.right
            elif x <= curr.data and curr.data <= y:
                ans += curr.left.size if curr.left else 0
                return ans
        return -1

    def preOrderNonRecursive(self):
        if not self.root:
            return ""
        
        stack = [self.root]
        result = []
        while stack:
            curr = stack.pop()
            result.append(str(curr.data))
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
                
        return " ".join(result)
    
def main():
    input_data = sys.stdin.read().split()

    iterator = iter(input_data)
    tree = AVL()
    
    for cmd in iterator:
        t = int(cmd)
        if t == 1:
            tree.insert(int(next(iterator)))
        elif t == 2:
            tree.delete(int(next(iterator)))
        elif t == 3:
            x, y = int(next(iterator)), int(next(iterator))
            write(f"{str(tree.getQuery(x, y))}\n")
        elif t == 4:
            write(f"{tree.preOrderNonRecursive()}\n")
 
if __name__ == '__main__':
    main()
