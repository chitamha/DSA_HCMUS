import sys
write = sys.stdout.write

def solve():
    global n, q, m, minCost
    root = 0
    for i in range(1, n):
        if q[root] < q[i]:
            root = i

    if q.count(q[root]) > 1:
        write("-1\n")
        return

    total = 0
    for i in range(n):
        if i == root:
            continue
        if minCost[i] == INF:
            write("-1\n")
            return
        total += minCost[i]
    
    write(str(total) + "\n")

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    q = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    # minCost[b] = chi phi nho nhat de b co 1 sep hop le
    INF = float('inf')
    minCost = [INF] * n
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        u, v = u-1, v-1
        if q[u] > q[v]:
            minCost[v] = min(minCost[v], w)
    
    solve()