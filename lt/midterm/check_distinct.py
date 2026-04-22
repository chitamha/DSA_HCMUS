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


def checkDistinct(n, arr):
    aux = [0] * n
    mergeSort(0, n - 1, arr, aux)

    for i in range(0, n - 1):
        if arr[i] == arr[i + 1]:
            return False
        
    return True

arr = list(map(int, input().split()))
print(checkDistinct(len(arr), arr))