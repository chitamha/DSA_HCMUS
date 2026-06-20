import sys
write = sys.stdout.write
sys.setrecursionlimit(2000000)

def solve(graph, n, m, positions):
    def inGraph(x, y, n, m):
        return x >= 0 and x < n and y >= 0 and y < m
    
    adjacent = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    answers = []
    visited = [[-1] * m for _ in range(n)]

    def dfs(graph, visited, x, y, n, m, idx):
        stack = [(x, y)]
        visited[x][y] = idx

        ans = 0
        while stack:
            x, y = stack.pop()

            for i, j in adjacent:
                new_x, new_y = x + i, y + j
                if inGraph(new_x, new_y, n, m):
                    if graph[new_x][new_y] == '*':
                        ans += 1
                    elif visited[new_x][new_y] == -1:
                        stack.append((new_x, new_y))
                        visited[new_x][new_y] = idx

        return ans

    idx = 0
    for x, y in positions:
        if visited[x][y] == -1:
            ans = dfs(graph, visited, x, y, n, m, idx)
            answers.append(ans)
            idx += 1
        else:
            ans = answers[visited[x][y]]
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
        positions.append((x, y))

    solve(graph, n, m, positions)

if __name__ == "__main__":
    main()