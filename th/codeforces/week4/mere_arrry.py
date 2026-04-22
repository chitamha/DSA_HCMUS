import sys

write = sys.stdout.write

def quickSort(l, r, arr):
    if l >= r:
        return

    p_idx = (l + r) // 2
    pivot = arr[p_idx]
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

def process(n, arr):
    comparisonArray = arr.copy()
    quickSort(0, n - 1, comparisonArray)
    minElement = comparisonArray[0]

    for i in range(n):
        if arr[i] % minElement != 0:
            if arr[i] != comparisonArray[i]:
                write(f"NO\n")
                return
    
    write(f"YES\n")

def main():
    t = int(sys.stdin.readline())
    for query in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        process(n, arr)

if __name__ == "__main__":
    main()