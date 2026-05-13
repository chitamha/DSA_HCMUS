import sys

write = sys.stdout.write

def merge(l, mid, r, arr, aux):
    i = l         # Con trỏ nữa trái
    j = mid + 1   # Con trỏ nữa phải
    k = l         # Con trỏ mảng phụ
    
    while i <= mid and j <= r:
        write(f"{i} {j}\n")
        if arr[i] <= arr[j]:
            aux[k] = arr[i]
            i += 1
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
    
    for p in range(l, r + 1):
        arr[p] = aux[p]

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
    
    aux = [0] * n
    mergeSort(0, n - 1, arr, aux)

if __name__ == '__main__':
    main()