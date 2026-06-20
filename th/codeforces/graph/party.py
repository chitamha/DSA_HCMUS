import sys
write = sys.stdout.write

def main():
    n = int(sys.stdin.readline())
    adj = [[] for _ in range(n + 1)]
    p = [0] * (n + 1)
    for i in range(1, n + 1):
        p[i] = int(sys.stdin.readline())
        if p[i] != -1:
            adj[p[i]].append(i)
    height = [-1] * (n + 1)

    def DFS(u):
        maxHeight = 0
        for v in adj[u]:
            if height[v] == -1:
                height[v] = height[u] + 1
                maxHeight = max(maxHeight, DFS(v))
        return maxHeight + 1
    
    totalGroups = 0
    for i in range(1, n + 1):
        if p[i] == -1:
            height[i] = 1
            totalGroups = max(totalGroups, DFS(i))
    write(str(totalGroups) + '\n')

if __name__ == "__main__":
    main()