import sys

def merge(l, mid, r, arr, aux):
    i, j, k = l, mid + 1, l
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            aux[k] = arr[i]
            k += 1
            i += 1
        else:
            aux[k] = arr[j]
            k += 1
            j += 1
    
    while i <= mid:
        aux[k] = arr[i]
        k += 1
        i += 1

    while j <= r:
        aux[k] = arr[j]
        k += 1
        j += 1
        
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
    input = sys.stdin.read().split()
    n = int(input[0])
    arr = []
    for i in range(n):
        word = input[i + 1]
        arr.append((len(word), word))

    aux = [(0, "")] * n
    mergeSort(0, n - 1, arr, aux)
    separator = '\n'
    sys.stdout.write(f"{separator.join(x[1] for x in arr)}")

if __name__ == "__main__":
    main()