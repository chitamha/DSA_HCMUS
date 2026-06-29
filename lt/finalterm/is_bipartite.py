import sys

def isBipartite(graph: list[list[int]]):
    global n
    color = [-1] * n
    
    for i in range(n):
        if color[i] == -1:
            if not bfs(graph, i, color):
                return False
    return True
    

def bfs(graph: list[list[int]], start: int, color: list[int]):
    queue = [start]
    color[start] = 0
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            if color[v] == -1:
                color[v] = color[u] ^ 1
                queue.append(v)
            elif color[v] == color[u]:
                return False
    return True

if __name__ == '__main__':
    n = int(input("Enter number of vertices: "))
    graph = []
    for i in range(n):
        graph.append(list(map(int, input("Enter neighbors: ").split())))
    print(isBipartite(graph))
    