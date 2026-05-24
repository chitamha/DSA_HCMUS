import sys
import bisect
write = sys.stdout.write

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    tempArr = sorted(arr)
    for i in range(n):
        idx = bisect.bisect_left(tempArr, arr[i])
        arr[i] = idx + 1

    bit = [0] * (n + 1)
    def update(pos, value):
        while pos <= n:
            bit[pos] += value
            pos += pos & (-pos)

    def get(pos):
        count = 0
        while pos >= 1:
            count += bit[pos]
            pos -= pos & (-pos)
        return count
    
    left = [0] * (n + 1)
    update(arr[0], 1)
    for i in range(1, n):
        left[i] = get(n) - get(arr[i])
        update(arr[i], 1)

    right = [0] * (n + 1)
    bit = [0] * (n + 1)
    update(arr[n - 1], 1)
    for i in range(n - 2, -1, -1):
        right[i] = get(arr[i] - 1)
        update(arr[i], 1)   

    ans = 0
    for idx in range(1, n - 1):
        # write(f"{left[idx]} {right[idx]} {ans}\n")
        ans += left[idx] * right[idx]
    
    write(f"{ans}")

if __name__ == "__main__":
    main()