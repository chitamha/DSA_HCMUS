import sys
write = sys.stdout.write

def merge(l, mid, r, arr, aux):
    i, j, k = l, mid + 1, l
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            aux[k] = arr[i]
            i += 1
            k += 1
        else:
            aux[k] = arr[j]
            j += 1
            k += 1

    while i <= mid:
        aux[k] = arr[i]
        i += 1
        k += 1

    while j <= r:
        aux[k] = arr[j]
        j += 1
        k += 1

    for idx in range(l, r + 1):
        arr[idx] = aux[idx]

def mergeSort(l, r, arr, aux):
    if l >= r:
        return
    
    mid = (l + r) // 2
    mergeSort(l, mid, arr, aux)
    mergeSort(mid + 1, r, arr, aux)
    merge(l, mid, r, arr, aux)

def lowerBound(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= x:
            right = mid - 1
        else:
            left = mid + 1
    return right + 1

def solve():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    ans, aux = 0, [0] * m
    # mergeSort(0, m - 1, b, aux)
    for i in range(0, n):
        curDis, idxLowerBound = int(1e10), lowerBound(b, a[i])
        if idxLowerBound < len(b):
            curDis = b[idxLowerBound] - a[i]
        if idxLowerBound >= 1:
            curDis = min(curDis, a[i] - b[idxLowerBound - 1])
        ans = max(ans, curDis)

        # write(f"{b[idxLowerBound] - a[i]}")
        # if idxLowerBound >= 1:
        #     write(f" {a[i] - b[idxLowerBound - 1]}")
        # write(f"\n")

    write(f"{ans}\n")

if __name__ == "__main__":
    solve()