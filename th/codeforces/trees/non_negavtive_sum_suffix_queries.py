import sys

# Tăng giới hạn đệ quy cho Segment Tree
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    q = int(input_data[0])
    
    # Tree lưu giá trị max của Prefix Sums
    MAXN = q + 5
    tree = [-float('inf')] * (4 * MAXN)
    p = [0] * MAXN
    
    def update(node, start, end, idx, val):
        if start == end:
            tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            update(2 * node, start, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, end, idx, val)
            
        left_val = tree[2 * node]
        right_val = tree[2 * node + 1]
        tree[node] = left_val if left_val > right_val else right_val

    def query(node, start, end, l, r, threshold):
        if r < start or end < l or tree[node] <= threshold:
            return -1
        
        if start == end:
            return start
        
        mid = (start + end) // 2
        
        res = query(2 * node + 1, mid + 1, end, l, r, threshold)
        if res != -1:
            return res
            
        return query(2 * node, start, mid, l, r, threshold)

    ptr = 1 # Con trỏ dữ liệu
    cur = 0 # Chỉ số cuối hiện tại
    start = 1 # Chỉ số đầu hiện tại
    
    # Cập nhật gốc P[0] = 0. Segment tree chạy từ 0 đến MAXN - 1
    update(1, 0, MAXN - 1, 0, 0)
    
    results = []
    
    for _ in range(q):
        type_query = int(input_data[ptr])
        ptr += 1
        
        if type_query == 1:
            val = int(input_data[ptr])
            ptr += 1
            cur += 1
            p[cur] = p[cur - 1] + val
            update(1, 0, MAXN - 1, cur, p[cur])
            
        elif type_query == 2:
            start += 1
            
        else:
            # Tìm index xa nhất trong [start-1, cur-1] sao cho P[idx] > P[cur]
            idx = query(1, 0, MAXN - 1, start - 1, cur - 1, p[cur])
            
            if idx == -1:
                results.append(str(cur - start + 1))
            else:
                results.append(str(cur - idx - 1))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()