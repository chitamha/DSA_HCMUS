def topoSort(aList, n, adj):
    



def main():
    n, m = map(int, input().split())

    adj = [[0] for _ in range(n + 1)]
    for i in range(m):
        u, v = map(int, input.split())
        adj[u][v] = 1

    aList = []
    topoSort(aList, n, adj)