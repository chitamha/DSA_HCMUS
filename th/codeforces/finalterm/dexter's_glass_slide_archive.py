import sys

class SegmentTree:
    def __init__(self, n):
        # Lưu bitmask tại mỗi node, khởi tạo mảng 0
        self.T = [0] * (4 * (n + 5))
    
    def build(self, id, l, r, arr):
        if l == r:
            self.T[id] = 1 << arr[l]  # Bật bit thứ arr[l]
            return
        mid = (l + r) // 2
        self.build(2 * id, l, mid, arr)
        self.build(2 * id + 1, mid + 1, r, arr)
        # Gộp 2 nhánh bằng phép OR
        self.T[id] = self.T[2 * id] | self.T[2 * id + 1]

    def update(self, id, l, r, pos, newValue):
        if l == r:
            self.T[id] = 1 << newValue
            return
        mid = (l + r) // 2
        if pos <= mid:
            self.update(2 * id, l, mid, pos, newValue)
        else:
            self.update(2 * id + 1, mid + 1, r, pos, newValue)
        self.T[id] = self.T[2 * id] | self.T[2 * id + 1]
    
    def get(self, id, l, r, u, v):
        if u > r or v < l:
            return 0
        if u <= l and r <= v:
            return self.T[id]
        mid = (l + r) // 2
        # Gộp kết quả 2 nhánh bằng phép OR thay vì dấu +
        return self.get(2 * id, l, mid, u, v) | self.get(2 * id + 1, mid + 1, r, u, v)

def solve():
    # Đọc input nhanh toàn bộ để tránh TLE
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    q = int(input_data[1])
    arr = [int(x) for x in input_data[2:2+n]]

    tree = SegmentTree(n)
    tree.build(1, 0, n - 1, arr)
    
    out = []
    idx = 2 + n
    for _ in range(q):
        cmd = int(input_data[idx])
        if cmd == 1:
            p = int(input_data[idx+1])
            x = int(input_data[idx+2])
            tree.update(1, 0, n - 1, p - 1, x)
            idx += 3
        else:
            l = int(input_data[idx+1])
            r = int(input_data[idx+2])
            mask = tree.get(1, 0, n - 1, l - 1, r - 1)
            # Đếm số lượng bit 1 trong mask
            out.append(str(bin(mask).count('1')))
            idx += 3
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == "__main__":
    solve()