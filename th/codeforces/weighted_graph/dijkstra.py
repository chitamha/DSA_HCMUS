import sys
import heapq
write = sys.stdout.write

def dijkstra(root):
    global dis, adj, before
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
                before[v] = u
                heapq.heappush(pq, (dis[v], v))

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    dis = [float('inf')] * (n + 1)
    before = [0] * (n + 1)
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    dijkstra(1)
    if dis[n] == float('inf'):
        write("-1")
    else:
        path = []
        current = n
        while current != 0:
            path.append(current)
            current = before[current]
        path.reverse()
        write(" ".join(map(str, path)))