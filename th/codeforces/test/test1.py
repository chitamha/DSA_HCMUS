import sys

def solve():
    # Sử dụng generator để đọc input nhằm tối ưu hóa bộ nhớ (< 32MB)
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token
    
    tokens = get_tokens()
    try:
        q_str = next(tokens)
    except StopIteration:
        return
    q = int(q_str)
    
    # Kích thước mảng cho Segment Tree (lũy thừa của 2 gần nhất)
    M = 1
    while M <= q + 5:
        M *= 2
        
    INF = 10**18
    tree = [-INF] * (2 * M)
    
    # Cập nhật điểm trên Segment Tree
    def update(idx, val):
        idx += M
        tree[idx] = val
        idx //= 2
        while idx > 0:
            left = tree[2 * idx]
            right = tree[2 * idx + 1]
            tree[idx] = left if left > right else right
            idx //= 2

    P = [0] * (q + 5)
    R = 0
    L = 1
    update(0, 0)
    
    out = []
    for _ in range(q):
        type_query = int(next(tokens))
        
        if type_query == 1:
            x = int(next(tokens))
            R += 1
            P[R] = P[R-1] + x
            update(R, P[R])
            
        elif type_query == 2:
            L += 1
            
        elif type_query == 3:
            l_bound = L - 1
            r_bound = R - 1
            v = P[R]
            
            ll = l_bound + M
            rr = r_bound + M
            
            nodes_left = []
            nodes_right = []
            
            # Phân tách các node bao phủ đoạn [l_bound, r_bound]
            while ll <= rr:
                if ll % 2 == 1:
                    nodes_left.append(ll)
                    ll += 1
                if rr % 2 == 0:
                    nodes_right.append(rr)
                    rr -= 1
                ll //= 2
                rr //= 2
            
            m_found = -1
            
            # Quét từ phải sang trái để tìm rightmost index > v
            # 1. Quét các node mảng phải
            for node in nodes_right:
                if tree[node] > v:
                    curr = node
                    while curr < M:
                        if tree[2 * curr + 1] > v:
                            curr = 2 * curr + 1
                        else:
                            curr = 2 * curr
                    m_found = curr - M
                    break
            
            # 2. Nếu chưa thấy, quét các node mảng trái (theo thứ tự ngược lại)
            if m_found == -1:
                for i in range(len(nodes_left) - 1, -1, -1):
                    node = nodes_left[i]
                    if tree[node] > v:
                        curr = node
                        while curr < M:
                            if tree[2 * curr + 1] > v:
                                curr = 2 * curr + 1
                            else:
                                curr = 2 * curr
                        m_found = curr - M
                        break
                        
            # Tính toán kết quả
            if m_found != -1:
                out.append(str(R - m_found - 1))
            else:
                out.append(str(R - L + 1))
                
    # In toàn bộ kết quả một lần
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()