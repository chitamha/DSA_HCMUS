import sys
write = sys.stdout.write
sys.setrecursionlimit(200000)

def solve():
    n, t = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    a.insert(0, 0)
    adj = [[] for _ in range(n + 5)]
    for i in range(1, n):
        adj[i].append(a[i] + i)

    visited = [False] * (n + 5)
    def dfs(u):
        if u == t:
            return True
        visited[u] = True

        for v in adj[u]:
            if visited[v] is False:
                if dfs(v):
                    return True
                
        return False
    
    write(f"{"YES" if dfs(1) else "NO"}\n")

if __name__ == "__main__":
    solve()