#include <iostream>
#include <vector>

using namespace std;

struct Edge {
    int to;
    int id;
};

const int MAX_V = 1000005;
const int MAX_E = 2000005; // Chứa m cạnh thật + n cạnh ảo

vector<Edge> adj[MAX_V];
bool used[MAX_E];
int u_edge[MAX_E];
int v_edge[MAX_E];
int deg[MAX_V];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    for (int i = 1; i <= m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back({v, i});
        adj[v].push_back({u, i});
        deg[u]++;
        deg[v]++;
        u_edge[i] = u;
        v_edge[i] = v;
    }

    // Thêm đỉnh ảo 0 để nối với các đỉnh bậc lẻ
    int edge_cnt = m;
    for (int i = 1; i <= n; i++) {
        if (deg[i] % 2 != 0) {
            edge_cnt++;
            adj[0].push_back({i, edge_cnt});
            adj[i].push_back({0, edge_cnt});
        }
    }

    vector<int> ans;

    // Tìm chu trình Euler trên toàn bộ đồ thị
    for (int i = 0; i <= n; i++) {
        if (adj[i].empty()) continue;

        vector<int> path;
        vector<pair<int, int>> st;
        st.push_back({i, -1});

        // Thuật toán Hierholzer lặp (tránh tràn Stack)
        while (!st.empty()) {
            int u = st.back().first;
            bool found = false;
            while (!adj[u].empty()) {
                auto [v, id] = adj[u].back();
                adj[u].pop_back();
                if (!used[id]) {
                    used[id] = true;
                    st.push_back({v, id});
                    found = true;
                    break;
                }
            }
            if (!found) {
                int id = st.back().second;
                st.pop_back();
                if (id != -1) path.push_back(id);
            }
        }

        if (path.empty()) continue;

        bool has_dummy = false;
        for (int id : path) {
            if (id > m) has_dummy = true;
        }

        // Nếu chu trình không có cạnh ảo (thuần tuý cạnh thật)
        if (!has_dummy) {
            for (size_t j = 0; j < path.size(); j++) {
                if (j % 2 == 0) ans.push_back(path[j]);
            }
        } 
        // Nếu chu trình có cạnh ảo
        else {
            int first_dummy_idx = -1;
            for (size_t j = 0; j < path.size(); j++) {
                if (path[j] > m) {
                    first_dummy_idx = j;
                    break;
                }
            }

            // Dịch vòng để mảng bắt đầu bằng một cạnh ảo
            vector<int> rotated;
            rotated.reserve(path.size());
            for (size_t j = first_dummy_idx; j < path.size(); j++) rotated.push_back(path[j]);
            for (size_t j = 0; j < first_dummy_idx; j++) rotated.push_back(path[j]);

            vector<int> real_edges;
            for (size_t j = 0; j < rotated.size(); j++) {
                if (rotated[j] > m) {
                    // Gặp cạnh ảo -> kết thúc một đoạn cạnh thật
                    if (!real_edges.empty()) {
                        for (size_t k = 0; k < real_edges.size(); k++) {
                            if (k % 2 == 0) ans.push_back(real_edges[k]);
                        }
                        if (real_edges.size() % 2 == 0) {
                            ans.push_back(real_edges.back());
                        }
                        real_edges.clear();
                    }
                } else {
                    real_edges.push_back(rotated[j]);
                }
            }
            // Xử lý đoạn cạnh thật cuối cùng (nếu có)
            if (!real_edges.empty()) {
                for (size_t k = 0; k < real_edges.size(); k++) {
                    if (k % 2 == 0) ans.push_back(real_edges[k]);
                }
                if (real_edges.size() % 2 == 0) {
                    ans.push_back(real_edges.back());
                }
            }
        }
    }

    // In kết quả
    cout << ans.size() << "\n";
    for (int id : ans) {
        cout << u_edge[id] << " " << v_edge[id] << "\n";
    }

    return 0;
}