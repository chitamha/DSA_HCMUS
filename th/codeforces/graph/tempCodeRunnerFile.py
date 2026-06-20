import sys
write = sys.stdout.write

def solve():
    n, t = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    adj = [[]] * (n + 5)
    for i in range(n - 1):
        adj[i + 1].append(a[i] + i + 1)

    visited = [False] * (n + 5)
    def dfs(u):
        if u == t:
            return 1
        visited[u] = 1

        for v in adj[u]:
            if visited[v] is False:
                if dfs(v):
                    return 1
                
        return 0
    
    write(f"{"YES" if dfs(1) else "NO"}\n")

if __name__ == "__main__":
    solve()