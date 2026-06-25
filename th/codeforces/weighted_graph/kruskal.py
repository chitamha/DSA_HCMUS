import sys
from array import array

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    # Store edges compactly: 3 parallel arrays instead of list of tuples
    ew = array('l', (int(data[idx + i * 3 + 2]) for i in range(m)))
    eu = array('l', (int(data[idx + i * 3    ]) for i in range(m)))
    ev = array('l', (int(data[idx + i * 3 + 1]) for i in range(m)))

    # Sort edges by weight using index sort
    order = sorted(range(m), key=lambda i: ew[i])

    # DSU with compact array storage
    parent = array('l', range(n + 1))
    rank   = array('b', [0] * (n + 1))  # 'b' = signed char (1 byte each)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]  # path halving
            x = parent[x]
        return x

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True

    total_weight = 0
    edges_used = 0

    for i in order:
        if union(eu[i], ev[i]):
            total_weight += ew[i]
            edges_used += 1
            if edges_used == n - 1:
                break

    print(-1 if edges_used < n - 1 else total_weight)

main()
