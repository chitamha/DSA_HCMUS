def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

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
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    quick_sort(arr, 0, n - 1)
    # print(arr)
    for x in queries:
        right_id = lower_bound(arr, x)
        if right_id - 1 >= 0 and right_id < n:
            if arr[right_id] - x <= x - arr[right_id - 1]:
                print(arr[right_id])
            else:
                print(arr[right_id - 1])
        elif (right_id - 1 < 0):
            print(arr[right_id])
        else:
            print(arr[right_id - 1])
    
main()