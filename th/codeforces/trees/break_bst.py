import sys
write = sys.stdout.write
sys.setrecursionlimit(200000)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def dfs(node, minValue, maxValue, validValues):
    if node is None:
        return
        
    # Dùng <= để bao quát đúng giá trị
    if minValue <= node.data <= maxValue:
        validValues.add(node.data)
        
    # Nhánh trái: Cập nhật lại giới hạn lớn nhất bằng min()
    dfs(node.left, minValue, min(maxValue, node.data), validValues)
    
    # Nhánh phải: Cập nhật lại giới hạn nhỏ nhất bằng max()
    dfs(node.right, max(minValue, node.data), maxValue, validValues)

def main():
    n = int(sys.stdin.readline())
    arr = [None for _ in range(n + 1)]
    parents = [0 for _ in range(n + 1)]
    for idx in range(1, n + 1):
        v, l, r = map(int, sys.stdin.readline().split())
        arr[idx] = (Node(v), l, r)

    for idx in range(1, n + 1):
        if arr[idx][1] != -1:
            arr[idx][0].left = arr[arr[idx][1]][0]
            parents[arr[idx][1]] = idx
        if arr[idx][2] != -1:
            arr[idx][0].right = arr[arr[idx][2]][0]
            parents[arr[idx][2]] = idx

    for idx in range(1, n + 1):
        if parents[idx] == 0:
            root = arr[idx][0]
            break

    ans, validValues = 0, set()
    dfs(root, -float('inf'), float('inf'), validValues)
    for idx in range(1, n + 1):
        if not (arr[idx][0].data in validValues):
            ans += 1

    write(f"{ans}")

main()