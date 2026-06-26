import sys

def partition(arr, low, high):
    i, j = low - 1, high + 1
    pivotIdx = (i + j) // 2
    pivot = arr[pivotIdx]
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            break
        
        arr[i], arr[j] = arr[j], arr[i]
        if i == pivotIdx:
            pivotIdx = j
        elif j == pivotIdx:
            pivotIdx = i


def solve():
    global n, k, arr


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split())
    arr = map(int, sys.stdin.readline().strip().split())
    solve()