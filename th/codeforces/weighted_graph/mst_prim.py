import sys
import heapq
write = sys.stdout.write

def prim(startVertex, graph):
    minEdges = [(cost, startVertex, to) for to, cost in graph[startVertex]]
    heapq.heapify(minEdges)
    visited = set([startVertex])
    totalCost = 0
    while minEdges:
        cost, fromVertex, toVertex = heapq.heappop(minEdges)
        if toVertex in visited:
            continue
        visited.add(toVertex)
        totalCost += cost
        for nextVertex, nextCost in graph[toVertex]:
            if nextVertex not in visited:
                heapq.heappush(minEdges, (nextCost, toVertex, nextVertex))

    flag = False
    for i in range(1, len(graph)):
        if i not in visited:
            flag = True
            break
    if flag:
        write("-1\n")
    else:
        write(f"{totalCost}\n")

if __name__ == "__main__":
    n, m, s = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    prim(s, adj)