import sys

write = sys.stdout.write

# Simple Quick Sort
def quickSortSimple(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quickSortSimple(left) + middle + quickSortSimple(right)

# Complicated Quick Sort
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
        
    
lis = list(map(int, input().split()))
# print(quick_sort_simple(lis))
quickSort(0, len(lis) - 1, lis)
print(lis)