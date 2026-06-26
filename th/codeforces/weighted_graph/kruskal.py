import sys
input = sys.stdin.readline
def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n, m = int(data[idx]), int(data[idx + 1])
    idx += 2
    edges = []
    for _ in range(m):
        u, v, w = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
        idx += 3
        if u != v:  # bỏ self-loop
            edges.append((w, u, v))
    # Sắp xếp theo trọng số
    edges.sort()
    # DSU (Disjoint Set Union) với path compression + union by rank
    parent = list(range(n + 1))
    rank   = [0] * (n + 1)
    def find(x):
        # Iterative path compression
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        return True
    total_weight = 0
    edge_count   = 0
    for w, u, v in edges:
        if union(u, v):
            total_weight += w
            edge_count   += 1
            if edge_count == n - 1:
                break
    if edge_count < n - 1:
        print(-1)
    else:
        print(total_weight)
main()