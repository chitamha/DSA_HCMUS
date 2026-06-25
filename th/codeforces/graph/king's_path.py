import sys
from collections import deque

def main():
    # Bước 1: Xử lý input, đưa ra tập hợp các ô được phép đi
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    r0, c0, r1, c1 = map(int, input_data[:4])
    n = int(input_data[4])

    allowed_cells = set()
    idx = 5
    for _ in range(n):
        r = int(input_data[idx])
        a = int(input_data[idx + 1])
        b = int(input_data[idx + 2])
        for c in range(a, b + 1):
            allowed_cells.add((r, c))
        idx += 3

    # Bước 2: Gọi BFS
    queue = deque([(r0, c0, 0)])

    # Đánh dấu đã thăm bằng cách xóa khỏi allowed_cells để tiết kiệm bộ nhớ và thời gian
    if (r0, c0) in allowed_cells:
        allowed_cells.remove((r0, c0))

    # 8 hướng di chuyển của quân Vua
    moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    while queue:
        curr_r, curr_c, dist = queue.popleft()

        if curr_r == r1 and curr_c == c1:
            print(dist)
            return

        for dr, dc in moves:
            nr, nc = curr_r + dr, curr_c + dc
            if (nr, nc) in allowed_cells:
                allowed_cells.remove((nr, nc))
                queue.append((nr, nc, dist + 1))

    print("-1")

if __name__ == "__main__":
    main()