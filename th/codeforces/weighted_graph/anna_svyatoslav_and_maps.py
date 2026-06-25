import sys
if __name__ == "__main__":
    n = int(input())
    INF = float('inf')
    # Đọc ma trận kề và khởi tạo ma trận khoảng cách cho Floyd-Warshall
    dist = []
    for i in range(n):
        row = list(map(int, input().strip()))
        dist.append([1 if row[j] == 1 else INF for j in range(n)])
    # Khoảng cách từ node đến chính nó = 0
    for i in range(n):
        dist[i][i] = 0
    # Floyd-Warshall: tìm khoảng cách ngắn nhất giữa mọi cặp đỉnh
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    m = int(input())
    p = list(map(int, input().split()))
    p = [x - 1 for x in p]  # chuyển về 0-indexed
    # Greedy: tìm dãy con ngắn nhất của p
    # Giữ lại p[i-1] nếu đường đi ngắn nhất từ p[last] đến p[i]
    # nhỏ hơn khoảng cách index (i - last_idx), tức là "nhảy cóc" sẽ đi sai đường
    ans = [p[0]]
    last_idx = 0
    for i in range(1, m):
        if dist[p[last_idx]][p[i]] < i - last_idx:
            ans.append(p[i - 1])
            last_idx = i - 1
    # Luôn thêm điểm cuối (nếu chưa có)
    if ans[-1] != p[m - 1]:
        ans.append(p[m - 1])
    print(len(ans))
    print(*[x + 1 for x in ans])  # in lại về 1-indexed