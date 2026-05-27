import sys
write = sys.stdout.write

class SegmentTree():
    def __init__(self, n):
        self.T = [-float('inf')] * (4*(n + 5))
    
    def insert(self, id, l, r, pos, value):
        if l == r:
            self.T[id] = value
            return
        
        mid = (l + r) // 2
        if pos <= mid:
            self.insert(2*id, l, mid, pos, value)
        else:
            self.insert(2*id + 1, mid + 1, r, pos, value)
        self.T[id] = max(self.T[2*id], self.T[2*id + 1])

    def get(self, id, l, r, u, v, threshold):
        if u > r or v < l or self.T[id] <= threshold:
            return -1
        
        if l == r:
            return r
        
        mid = (l + r) // 2
        res = self.get(2*id + 1, mid + 1, r, u, v, threshold)
        if res != -1:
            return res
        else:
            return self.get(2*id, l, mid, u, v, threshold)
        
def main():
    input_data = sys.stdin.read().strip()
    iterator = iter(input_data.split())
    q = int(next(iterator))
    cur_sum, MAXN = 0, 100005
    l, r = 1, 0
    tree = SegmentTree(MAXN)
    tree.insert(1, 0, MAXN, 0, 0)
    for cmd in iterator:
        if cmd == '1':
            cur_sum += int(next(iterator))
            r += 1
            tree.insert(1, 0, MAXN, r, cur_sum)
        elif cmd == '2':
            l += 1
        else:
            res = tree.get(1, 0, MAXN, l - 1, r - 1, cur_sum)
            if res == -1:
                write(f"{r - l + 1}\n")
            else:
                write(f"{r - res - 1}\n")

main()