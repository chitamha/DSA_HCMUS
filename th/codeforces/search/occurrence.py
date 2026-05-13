def parition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if (low <= high):
        pi = parition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    
def upper_bound(arr, val):
    l, r = 0, len(arr) - 1
    while (l <= r):
        mid = (l + r) // 2
        if arr[mid] > val:
            r = mid - 1
        else:
            l = mid + 1
    return r + 1

def lower_bound(arr, val):
    l, r = 0, len(arr) - 1
    while (l <= r):
        mid = (l + r) // 2
        if arr[mid] >= val:
            r = mid - 1
        else:
            l = mid + 1
    return r + 1

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr) - 1)

    frequence, val = 0, 0
    for x in arr:
        cur_frequence = upper_bound(arr, x) - lower_bound(arr, x)
        if cur_frequence > frequence:
            frequence = cur_frequence
            val = x

    print(val)

main()