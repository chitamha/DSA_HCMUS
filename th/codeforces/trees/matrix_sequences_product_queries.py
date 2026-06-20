import sys
write = sys.stdout.write

class Node():
    __slots__ = ['data', 'height', 'size', 'product', 'left', 'right']
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.size = 1
        self.product = data
        self.left = None
        self.right = None

def multiplicationMatrix(A, B):
    global n, M
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k] == 0: continue
            for j in range(n):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % M
    return C

class AVL():
    def __init__(self):
        self.root = None

    def getBalance(self, node):
        lh = node.left.height if node.left else 0
        rh = node.right.height if node.right else 0
        return rh - lh
    
    def update(self, node):
        leftHeight = node.left.height if node.left else 0
        rightHeight = node.right.height if node.right else 0
        node.height = max(leftHeight, rightHeight) + 1
        leftSize = node.left.size if node.left else 0
        rightSize = node.right.size if node.right else 0
        node.size = leftSize + rightSize + 1
        global n
        I = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            I[i][i] = 1
        matrixA = node.left.product if node.left else I
        matrixB = node.right.product if node.right else I
        node.product = multiplicationMatrix(multiplicationMatrix(matrixA, node.data), matrixB)
        return node
    
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

    def rebalance(self, node):
        bal = self.getBalance(node)
        if bal < -1:
            if self.getBalance(node.left) <= -1:
                node = self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                node = self.right_rotate(node)
        elif bal > 1:
            if self.getBalance(node.right) >= 1:
                node = self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                node = self.left_rotate(node)
        
        self.update(node)
        return node

    def insert(self, data, node, pos):
        if node is None:
            return Node(data)

        leftSize = node.left.size if node.left else 0

        if pos <= leftSize:
            node.left = self.insert(data, node.left, pos)
        else:
            node.right = self.insert(data, node.right, pos - leftSize - 1)
        
        return self.rebalance(node)
    
def query(node, l, r):
    global n
    def get_identity():
        I = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n): I[i][i] = 1
        return I

    if not node or l > r:
        return get_identity()

    if l <= 1 and node.size <= r:
        return node.product

    leftSize = node.left.size if node.left else 0
    res = get_identity()
    has_res = False

    # 1. Truy vấn phần nằm bên trái
    if l <= leftSize:
        res = query(node.left, l, min(r, leftSize))
        has_res = True
        
    # 2. Truy vấn tại nút hiện tại
    if l <= leftSize + 1 and r >= leftSize + 1:
        if has_res:
            res = multiplicationMatrix(res, node.data)
        else:
            res = node.data
            has_res = True
            
    # 3. Truy vấn phần nằm bên phải
    if r > leftSize + 1:
        right_res = query(node.right, max(1, l - leftSize - 1), r - leftSize - 1)
        if has_res:
            res = multiplicationMatrix(res, right_res)
        else:
            res = right_res

    return res

def main():
    avlTree = AVL()
    for _ in range(q):
        command = list(map(int, sys.stdin.readline().split()))
        if command[0] == 1:
            matrix = []
            for _ in range(n):
                row = list(map(int, sys.stdin.readline().split()))
                matrix.append(row)
            avlTree.root = avlTree.insert(matrix, avlTree.root, command[1])

        else:
            ansMatrix = query(avlTree.root, command[1], command[2])
            for idx in range(n):
                write(f"{' '.join(str(x) for x in ansMatrix[idx])}\n")

if __name__ == '__main__':
    q, n, M = map(int, sys.stdin.readline().split())
    main()