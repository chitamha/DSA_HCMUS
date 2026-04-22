import sys

write = sys.stdout.write

def merge(l, mid, r, arr, aux):
    i, j, k = l, mid + 1, l

    while i <= mid and j <= r:
        if arr[i][0] <= arr[j][0]:
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

    
    for i in range(l, r + 1):
        arr[i] = aux[i]


def mergeSort(l, r, arr, aux):
    if l >= r:
        return 
    
    mid = (l + r) // 2
    mergeSort(l, mid, arr, aux)
    mergeSort(mid + 1, r, arr, aux)

    merge(l, mid, r, arr, aux)

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        arr[i] = (arr[i], i)

    aux = [(0, 0)] * n
    mergeSort(0, n - 1, arr, aux)
    for i in range(n):
        write(f"{arr[i][1]} ")
    
if __name__ == "__main__":
    main()