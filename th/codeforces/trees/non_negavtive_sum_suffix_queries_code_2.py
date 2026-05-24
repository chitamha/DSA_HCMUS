import sys
write = sys.stdout.write

def solve():
    input_data = sys.stdin.read().strip()
    iterator = iter(input_data.split())
    q = int(next(iterator))

    T = [0] * (4 * (q + 1))
    arr = [0]
    def update(id, left, right, pos, val):
        if left == right:
            T[id] = pos
            return
        
        mid = (left + right) // 2
        if pos <= mid:
            update(2*id, left, mid, pos, val)
        else:
            update(2*id + 1, mid + 1, right, pos, val)
        if arr[T[2*id]] >= arr[T[2*id + 1]]:
            T[id] = T[2*id]
        else:
            T[id] = T[2*id + 1]
        
    def query(id, left, right, start, end):
        if start > right or end < left or arr[end] >= arr[T[id]]:
            return -1
        
        if left <= start and end <= right and arr[end] < arr[T[id]]:
            return T[id]

        mid = (left + right) // 2
        res = query(2*id + 1, mid + 1, right, start, end)
        if res != -1:
            return res
        else:
            return query(2*id, left, mid, start, end)

    stIdx, enIdx = 1, 0
    for cmd in iterator:
        t = int(cmd)
        if t == 1:
            x = int(next(iterator))
            enIdx += 1
            arr.append(x + arr[enIdx - 1])
            update(1, 1, q + 1, enIdx, arr[enIdx])
        elif t == 2:
            stIdx += 1
        else:
            res = query(1, 1, q + 1, stIdx, enIdx)
            write(str(enIdx - res) + '\n')
    
if __name__ == "__main__":
    solve()