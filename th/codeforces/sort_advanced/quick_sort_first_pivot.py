import sys

write = sys.stdout.write

def partition(arr, low, high):
    i, j = low - 1, high + 1
    pivot_idx = low
    pivot = arr[pivot_idx]
    while True:
        i += 1
        write(f"{min(i, pivot_idx)} {max(i, pivot_idx)}\n")
        while arr[i] < pivot:
            i += 1
            write(f"{min(i, pivot_idx)} {max(i, pivot_idx)}\n")
        
        j -= 1
        write(f"{min(j, pivot_idx)} {max(j, pivot_idx)}\n")
        while arr[j] > pivot:
            j -= 1
            write(f"{min(j, pivot_idx)} {max(j, pivot_idx)}\n")
        
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

        if i == pivot_idx:
            pivot_idx = j
        elif j == pivot_idx:
            pivot_idx = i

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi)
        quick_sort(arr, pi + 1, high)

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, n - 1)

if __name__ == "__main__":
    main()