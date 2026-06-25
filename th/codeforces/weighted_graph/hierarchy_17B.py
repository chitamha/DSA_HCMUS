import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    q = list(map(int, input().split()))  # qualification của n nhân viên
    m = int(input())

    # min_cost[b] = chi phí nhỏ nhất để node b có 1 sếp hợp lệ
    INF = float('inf')
    min_cost = [INF] * n

    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1; b -= 1  # chuyển về 0-indexed
        # a chỉ được làm sếp b nếu qual[a] > qual[b]
        if q[a] > q[b]:
            min_cost[b] = min(min_cost[b], c)

    # Tìm root: node có qualification cao nhất
    max_q = max(q)
    roots = [i for i in range(n) if q[i] == max_q]

    # Nếu có nhiều hơn 1 người cùng qual cao nhất → không thể tạo 1 cây duy nhất
    if len(roots) > 1:
        print(-1)
        return

    root = roots[0]

    # Tính tổng chi phí: mỗi node (trừ root) phải có đúng 1 sếp
    total = 0
    for i in range(n):
        if i == root:
            continue
        if min_cost[i] == INF:
            # Node i không có sếp hợp lệ nào → impossible
            print(-1)
            return
        total += min_cost[i]

    print(total)

solve()
