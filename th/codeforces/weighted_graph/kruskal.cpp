#include <bits/stdc++.h>
using namespace std;

// ── Fast I/O (fread-based) ────────────────────────────────────────────────────
namespace fastio {
    static char buf[1 << 22]; // 4 MB buffer
    static int  pos, len;

    void init() { len = fread(buf, 1, sizeof(buf), stdin); }

    inline long long readLL() {
        // skip non-numeric chars (space, newline, etc.)
        while (pos < len && buf[pos] != '-' && (buf[pos] < '0' || buf[pos] > '9'))
            pos++;
        if (pos >= len) return 0;
        bool neg = (buf[pos] == '-');
        if (neg) pos++;
        long long x = 0;
        while (pos < len && buf[pos] >= '0' && buf[pos] <= '9')
            x = x * 10 + (buf[pos++] - '0');
        return neg ? -x : x;
    }

    inline int readInt() { return (int)readLL(); }
}

// ── DSU ───────────────────────────────────────────────────────────────────────
static int parent[200005];
static int rnk[200005];

inline int find(int x) {
    while (parent[x] != x) {
        parent[x] = parent[parent[x]]; // path halving
        x = parent[x];
    }
    return x;
}

inline bool unite(int x, int y) {
    int px = find(x), py = find(y);
    if (px == py) return false;
    if (rnk[px] < rnk[py]) swap(px, py);
    parent[py] = px;
    if (rnk[px] == rnk[py]) rnk[px]++;
    return true;
}

// ── Edge (dùng long long cho weight) ─────────────────────────────────────────
struct Edge {
    long long w;
    int u, v;
    bool operator<(const Edge& o) const { return w < o.w; }
};

// ── Main ──────────────────────────────────────────────────────────────────────
int main() {
    fastio::init();

    int n = fastio::readInt();
    int m = fastio::readInt();

    vector<Edge> edges(m);
    for (auto& e : edges) {
        e.u = fastio::readInt();
        e.v = fastio::readInt();
        e.w = fastio::readLL();   // long long để tránh overflow
    }

    sort(edges.begin(), edges.end()); // O(m log m)

    iota(parent + 1, parent + n + 1, 1); // parent[i] = i

    long long total = 0;
    int used = 0;

    for (auto& e : edges) {
        if (unite(e.u, e.v)) {
            total += e.w;
            if (++used == n - 1) break;
        }
    }

    printf("%lld\n", used < n - 1 ? -1LL : total);
    return 0;
}
