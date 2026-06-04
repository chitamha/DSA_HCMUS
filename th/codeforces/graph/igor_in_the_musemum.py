import sys
write = sys.stdout.write

def dfs(graph, visited, adjacents, x, y, n, m):
    if x < 0 or x >= n or y < 0 or y >= m or visited[x][y]:
        return
    visited[x][y] = True
    if graph[x][y] == '*':
        adjacents.append((x, y))
        return
    dfs(graph, visited, adjacents, x + 1, y, n, m)
    dfs(graph, visited, adjacents, x - 1, y, n, m)
    dfs(graph, visited, adjacents, x, y + 1, n, m)
    dfs(graph, visited, adjacents, x, y - 1, n, m)

def inGraph(x, y, n, m):
    return x >= 0 and x < n and y >= 0 and y < m

def solve(graph, n, m, positions):
    for x, y in positions:
        visited = [[False] * m for _ in range(n)]
        adjacents = []
        dfs(graph, visited, adjacents, x, y, n, m)
        ans = 0
        for x, y in adjacents:
            write(f"({x + 1}, {y + 1})\n")
            if inGraph(x + 1, y, n, m) and (graph[x + 1][y] == '.' or graph[x + 1][y] == '1'):
                ans += 1
            if inGraph(x - 1, y, n, m) and (graph[x - 1][y] == '.' or graph[x - 1][y] == '1'):
                ans += 1
            if inGraph(x, y + 1, n, m) and (graph[x][y + 1] == '.' or graph[x][y + 1] == '1'):
                ans += 1
            if inGraph(x, y - 1, n, m) and (graph[x][y - 1] == '.' or graph[x][y - 1] == '1'):
                ans += 1
        write(f"{ans}\n")

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(n):
        row = list(map(str, sys.stdin.readline().strip()))
        graph.append(row)

    positions = []
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        x -= 1
        y -= 1
        graph[x][y] = '1'
        positions.append((x, y))

    solve(graph, n, m, positions)

if __name__ == "__main__":
    main()