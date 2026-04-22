import bisect

def update(n, pos, val):
    while (pos <= n):
        Bit[pos] += val
        pos += pos & (-pos)

def get(pos):
    sum = 0
    while (pos > 0):
        sum += Bit[pos]
        pos -= pos & (-pos)
    return sum

def compress_arr(arr):
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        arr[i] = bisect.bisect_left(sorted_arr, arr[i])

n = int(input())
Bit = [0] * (n + 10)

arr = list(map(int, input().split()))
compress_arr(arr)

ans = 0
for i in range(n - 1, -1, -1):
    ans += get(arr[i])
    update(n, arr[i] + 1, 1)

print(ans)
