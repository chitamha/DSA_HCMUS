import sys
from collections import deque
def solve():
    data = sys.stdin.read().split()
    idx = 0
    N, M = int(data[idx]), int(data[idx + 1])
    idx += 2
    G_cost, S_cost = int(data[idx]), int(data[idx + 1])
    idx += 2
    edges = []
    for i in range(M):
        x, y, g, s = (
            int(data[idx]),
            int(data[idx + 1]),
            int(data[idx + 2]),
            int(data[idx + 3]),
        )
        idx += 4
        if x != y:  # bỏ self-loop (không giúp kết nối)
            edges.append((g, s, x - 1, y - 1, i))
    # Sắp xếp theo g tăng dần
    edges.sort()
    # ── Spanning tree duy trì theo s (minimum s-value spanning tree) ──
    # tree_adj[u] = list of (v, s_val, edge_id)
    tree_adj = [[] for _ in range(N)]
    num_tree_edges = 0
    # Union-Find để kiểm tra kết nối nhanh
    uf = list(range(N))
    def find(x):
        while uf[x] != x:
            uf[x] = uf[uf[x]]
            x = uf[x]
        return x
    def connected_uf(x, y):
        return find(x) == find(y)
    def union_uf(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            uf[rx] = ry
            return True
        return False
    def find_max_edge_on_path(start, end):
        """BFS trên cây hiện tại, tìm cạnh có s lớn nhất trên đường start→end.
        Trả về (u, v, s_val, eid) hoặc None nếu không có đường."""
        if start == end:
            return None
        # visited[node] = (parent, s_val, eid) hoặc None (cho start)
        visited = {start: None}
        queue = deque([start])
        found = False
        while queue and not found:
            node = queue.popleft()
            for neighbor, s_val, eid in tree_adj[node]:
                if neighbor not in visited:
                    visited[neighbor] = (node, s_val, eid)
                    if neighbor == end:
                        found = True
                        break
                    queue.append(neighbor)
        if end not in visited:
            return None
        # Truy vết ngược, tìm cạnh max s
        max_s = -1
        max_info = None
        curr = end
        while visited[curr] is not None:
            pnode, s_val, eid = visited[curr]
            if s_val > max_s:
                max_s = s_val
                max_info = (pnode, curr, s_val, eid)
            curr = pnode
        return max_info
    def remove_tree_edge(u, v, eid):
        tree_adj[u] = [(nb, sv, ei) for nb, sv, ei in tree_adj[u] if ei != eid]
        tree_adj[v] = [(nb, sv, ei) for nb, sv, ei in tree_adj[v] if ei != eid]
    def add_tree_edge(u, v, s_val, eid):
        tree_adj[u].append((v, s_val, eid))
        tree_adj[v].append((u, s_val, eid))
    def get_max_s_in_tree():
        max_s = 0
        for u in range(N):
            for _, s_val, _ in tree_adj[u]:
                if s_val > max_s:
                    max_s = s_val
        return max_s
    ans = -1
    i = 0
    total = len(edges)
    while i < total:
        g_val = edges[i][0]
        # Xử lý tất cả cạnh có cùng g_val
        while i < total and edges[i][0] == g_val:
            g, s, u, v, eid = edges[i]
            if not connected_uf(u, v):
                # u và v thuộc 2 thành phần khác → thêm vào cây
                add_tree_edge(u, v, s, eid)
                union_uf(u, v)
                num_tree_edges += 1
            else:
                # u và v đã kết nối → thử cải thiện bằng cách thay cạnh s lớn nhất
                max_edge = find_max_edge_on_path(u, v)
                if max_edge is not None and max_edge[2] > s:
                    pu, pv, ps, peid = max_edge
                    remove_tree_edge(pu, pv, peid)
                    add_tree_edge(u, v, s, eid)
            i += 1
        # Kiểm tra nếu cây đã bao trùm N đỉnh
        if num_tree_edges == N - 1:
            b = get_max_s_in_tree()
            cost = g_val * G_cost + b * S_cost
            if ans == -1 or cost < ans:
                ans = cost
    print(ans)
solve()
