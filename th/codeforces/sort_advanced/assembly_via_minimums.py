import sys

write = sys.stdout.write

def quickSort(l, r, arr):
    if l >= r:
        return

    pivot = arr[(l + r) // 2]
    i, j = l, r
    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]
        i, j = i + 1, j - 1
    
    quickSort(l, j, arr)
    quickSort(j + 1, r, arr)

def main():
    t = int(sys.stdin.readline())
    for query in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))

        quickSort(0, n*(n - 1) // 2 - 1, arr)
        orginalArr = []
        step = n - 2
        idx = 0
        while idx < n*(n - 1) // 2:
            orginalArr.append(arr[idx])
            for _ in range(step):
                idx += 1
            step -= 1
            idx += 1
        orginalArr.append(arr[idx - 1])
        
        write(f"{' '.join([str(x) for x in orginalArr])}\n")

if __name__ == "__main__":
    main()