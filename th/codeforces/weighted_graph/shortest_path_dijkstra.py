import sys
import heapq
write = sys.stdout.write

def dijkstra(root):
    global dis, adj
    pq = [(0, root)]
    heapq.heapify(pq)
    dis[root] = 0
    while pq:
        d, u = heapq.heappop(pq)
        if d > dis[u]:
            continue
        for v, w in adj[u]:
            if dis[v] > dis[u] + w:
                dis[v] = dis[u] + w
                heapq.heappush(pq, (dis[v], v))

if __name__ == "__main__":
    n, m, s = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    dis = [float('inf')] * (n + 1)
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))

    dijkstra(s)
    for i in range(1, n + 1):
        if dis[i] == float('inf'):
            write("-1 ")
        else:
            write(f"{dis[i]} ")