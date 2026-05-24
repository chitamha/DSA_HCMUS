import sys
import bisect
write = sys.stdout.write

def solve():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.insert(0, 0)

    T = [[] for i in range(4 * n + 10)]
    def build(id, l, r):
        if l == r:
            T[id] = [arr[l]]
            return

        mid = (l + r) // 2
        build(2*id, l, mid)
        build(2*id + 1, mid + 1, r)
        
        # Hợp nhất 2 mảng con đã sắp xếp
        i, j = 0, 0
        while i < len(T[2*id]) and j < len(T[2*id + 1]):
            if T[2*id][i] <= T[2*id + 1][j]:
                T[id].append(T[2*id][i])
                i += 1
            else:
                T[id].append(T[2*id + 1][j])
                j += 1
            
        while i < len(T[2*id]):
            T[id].append(T[2*id][i])
            i += 1

        while j < len(T[2*id + 1]):
            T[id].append(T[2*id + 1][j])
            j += 1

    def getLarger(id, l, r, u, v, targetValue):
        if v < l or u > r:
            return 0
        
        if u <= l and r <= v:
            return len(T[id]) - bisect.bisect_right(T[id], targetValue)
        
        mid = (l + r) // 2
        return getLarger(2*id, l, mid, u, v, targetValue) + getLarger(2*id + 1, mid + 1, r, u, v, targetValue)

    def getSmaller(id, l, r, u, v, targetValue):
        if v < l or u > r:
            return 0
        
        if u <= l and r <= v:
            return bisect.bisect_left(T[id], targetValue)
        
        mid = (l + r) // 2
        return getSmaller(2*id, l, mid, u, v, targetValue) + getSmaller(2*id + 1, mid + 1, r, u, v, targetValue)

    build(1, 1, n)

    # for i in range(1, 4*n + 5):
    #     write(f"{i} {' '.join(str(x) for x in T[i])}\n")

    ans = 0
    for i in range(2, n):
        # write(f"{getLarger(1, 1, n, 1, i - 1,  arr[i])} {getSmaller(1, 1, n, i + 1, n, arr[i])}\n")
        ans += getLarger(1, 1, n, 1, i - 1,  arr[i]) * getSmaller(1, 1, n, i + 1, n, arr[i])

    write(f"{ans}")

solve()