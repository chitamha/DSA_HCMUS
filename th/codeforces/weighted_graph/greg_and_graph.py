import sys
input = sys.stdin.readline

def main():
    INF = float('inf')
    n = int(input())

    a = []
    for _ in range(n):
        row = list(map(int, input().split()))
        a.append(row)  # 0-indexed

    order = list(map(int, input().split()))
    order = [x - 1 for x in order]  # chuyển sang 0-indexed

    # dist[i][j]: shortest path trong tập đỉnh đã thêm vào
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    S = []        # tập đỉnh đang hoạt động
    ans = [0] * n

    # Duyệt ngược: thêm đỉnh thay vì xóa
    for step in range(n - 1, -1, -1):
        k = order[step]

        # Bước 1: Khởi tạo dist[k][v] và dist[v][k] = cạnh trực tiếp
        for v in S:
            dist[k][v] = a[k][v]
            dist[v][k] = a[v][k]

        # Bước 2: Relax đường đi k->...->v và v->...->k qua các đỉnh trong S
        for m in S:
            for v in S:
                new_kv = dist[k][m] + dist[m][v]
                if new_kv < dist[k][v]:
                    dist[k][v] = new_kv

                new_vk = dist[v][m] + dist[m][k]
                if new_vk < dist[v][k]:
                    dist[v][k] = new_vk

        # Bước 3: Cập nhật mọi cặp (i, j) trong S đi qua đỉnh k mới
        for i in S:
            for j in S:
                new_ij = dist[i][k] + dist[k][j]
                if new_ij < dist[i][j]:
                    dist[i][j] = new_ij

        S.append(k)

        # Tính tổng shortest path trong S
        total = 0
        for i in S:
            for j in S:
                if i != j:
                    total += dist[i][j]

        ans[step] = total

    print(*ans)

main()