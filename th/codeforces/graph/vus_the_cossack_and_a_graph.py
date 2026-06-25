import sys

# Tăng giới hạn đệ quy nếu cần, nhưng bài này ta dùng vòng lặp để tránh tràn stack
sys.setrecursionlimit(2000000)

def solve():
    # Sử dụng generator để đọc dữ liệu giúp tiết kiệm bộ nhớ
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield int(word)
    
    tokens = get_input()
    
    try:
        n = next(tokens)
        m = next(tokens)
    except StopIteration:
        return
    
    # Danh sách kề: Lưu dưới dạng (v << 22 | edge_id) để giảm overhead của việc tạo list nhỏ
    # Với m <= 10^6, edge_id cần 20 bit, v <= 10^6 cần 20 bit. Dùng 22 bit cho an toàn.
    adj = [[] for _ in range(n + 1)]
    deg = [0] * (n + 1)
    edges_u = [0] * (m + 1)
    edges_v = [0] * (m + 1)
    
    for i in range(1, m + 1):
        u = next(tokens)
        v = next(tokens)
        adj[u].append((v << 22) | i)
        adj[v].append((u << 22) | i)
        deg[u] += 1
        deg[v] += 1
        edges_u[i] = u
        edges_v[i] = v
        
    # Thêm đỉnh ảo 0 nối với các đỉnh bậc lẻ
    virtual_id = m + 1
    for i in range(1, n + 1):
        if deg[i] % 2 != 0:
            adj[0].append((i << 22) | virtual_id)
            adj[i].append((0 << 22) | virtual_id)
            virtual_id += 1
            
    # Dùng bytearray để đánh dấu cạnh đã dùng (tiết kiệm bộ nhớ hơn list)
    used = bytearray(virtual_id + 1)
    ans_edges = []
    
    # Duyệt qua các đỉnh để tìm các chu trình/đường đi Euler
    # Ưu tiên duyệt từ đỉnh 0 trước để ngắt các đường đi tại đỉnh ảo
    nodes_to_process = [0] + list(range(1, n + 1))
    
    for i in nodes_to_process:
        while adj[i]:
            # Loại bỏ các cạnh đã sử dụng ở cuối list adj
            while adj[i] and used[adj[i][-1] & 0x3FFFFF]:
                adj[i].pop()
            if not adj[i]:
                break
            
            # Bắt đầu một chuyến đi (walk)
            combined = adj[i].pop()
            v_curr = combined >> 22
            eid_curr = combined & 0x3FFFFF
            used[eid_curr] = 1
            
            walk = []
            if eid_curr <= m:
                walk.append(eid_curr)
            
            curr = v_curr
            while True:
                while adj[curr] and used[adj[curr][-1] & 0x3FFFFF]:
                    adj[curr].pop()
                if not adj[curr]:
                    break
                
                combined_next = adj[curr].pop()
                v_next = combined_next >> 22
                eid_next = combined_next & 0x3FFFFF
                used[eid_next] = 1
                
                if eid_next <= m:
                    walk.append(eid_next)
                else:
                    # Nếu gặp cạnh ảo, xử lý đoạn cạnh thực hiện tại và reset
                    if walk:
                        L = len(walk)
                        for j in range(0, L, 2):
                            ans_edges.append(walk[j])
                        if L % 2 == 0:
                            ans_edges.append(walk[-1])
                        walk = []
                curr = v_next
            
            # Xử lý đoạn cạnh thực cuối cùng của chuyến đi
            if walk:
                L = len(walk)
                for j in range(0, L, 2):
                    ans_edges.append(walk[j])
                if L % 2 == 0:
                    ans_edges.append(walk[-1])

    # Xuất kết quả
    sys.stdout.write(f"{len(ans_edges)}\n")
    out = []
    for eid in ans_edges:
        out.append(f"{edges_u[eid]} {edges_v[eid]}")
        if len(out) > 10000: # Buffering output
            sys.stdout.write("\n".join(out) + "\n")
            out = []
    if out:
        sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    solve()