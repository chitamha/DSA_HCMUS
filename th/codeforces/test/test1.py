import sys

# Increase recursion depth for Quick Sort
sys.setrecursionlimit(200000)

def custom_compare(a, b):
    # Returns True if 'a' should come strictly before 'b'
    if len(a) != len(b):
        return len(a) < len(b)
    return a < b

def partition(arr, low, high):
    # Use middle element as pivot
    mid = low + (high - low) // 2
    arr[mid], arr[high] = arr[high], arr[mid]
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if custom_compare(arr[j], pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def solve():
    n = int(sys.stdin.readline())
    if n == 0:
        return
    
    strings = []
    for i in range(n):
        str = sys.stdin.readline()
        strings.append(str)
    
    # Run the custom sort
    quick_sort(strings, 0, n - 1)
    
    sys.stdout.write(''.join(strings))

if __name__ == '__main__':
    solve()