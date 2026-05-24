import sys
write = sys.stdout.write

def solve():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    iterator = iter(input_data.split())
    q = int(next(iterator))

    # Cây lưu giá trị MAX, kích thước 4 * (q + 5) để bao hàm cả vị trí 0
    T = [-float('inf')] * (4 * (q + 5))
    arr = [0] * (q + 5)
    
    def update(id, left, right, pos, val):
        if left == right:
            T[id] = val
            return
        
        mid = (left + right) // 2
        if pos <= mid:
            update(2*id, left, mid, pos, val)
        else:
            update(2*id + 1, mid + 1, right, pos, val)
        T[id] = max(T[2*id], T[2*id + 1])
        
    def query(id, left, right, q_left, q_right, threshold):
        # Tách biệt rõ ràng ranh giới truy vấn (q_left, q_right) và ngưỡng (threshold)
        if q_left > right or q_right < left or T[id] <= threshold:
            return -1
        
        if left == right:
            return left

        mid = (left + right) // 2
        # Ưu tiên đệ quy nhánh phải trước để lấy vị trí lớn nhất
        res = query(2*id + 1, mid + 1, right, q_left, q_right, threshold)
        if res != -1:
            return res
        return query(2*id, left, mid, q_left, q_right, threshold)

    stIdx, enIdx = 1, 0
    # Đưa giá trị tiền tố tại vị trí 0 vào cây
    update(1, 0, q, 0, 0)
    
    for cmd in iterator:
        t = int(cmd)
        if t == 1:
            x = int(next(iterator))
            enIdx += 1
            arr[enIdx] = arr[enIdx - 1] + x
            update(1, 0, q, enIdx, arr[enIdx])
        elif t == 2:
            stIdx += 1
        else:
            # Truy vấn trên đoạn [stIdx - 1, enIdx - 1] với threshold là arr[enIdx]
            res = query(1, 0, q, stIdx - 1, enIdx - 1, arr[enIdx])
            if res == -1:
                write('0\n')
            else:
                write(str(enIdx - res) + '\n')
    
if __name__ == "__main__":
    solve()