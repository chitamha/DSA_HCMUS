import sys

write = sys.stdout.write

def insertion_sort(arr, l, r):
    for i in range(l + 1, r + 1):
        key = arr[i]
        j = i - 1

        while j >= l:
            write(f"{j} {i}\n")
            if arr[j] <= key:
                break
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key

def merge(arr, l, mid, r):
    left = arr[l:mid + 1]
    right = arr[mid + 1:r + 1]
    i = j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            write(f"{min(i + l, j + mid + 1)} {max(i + l, j + mid + 1)}\n")
            i += 1
        else:
            arr[k] = right[j]
            write(f"{min(i + l, j + mid + 1)} {max(i + l, j + mid + 1)}\n")
            j += 1
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def hybrid_sort(arr, l, r):
    if l < r:
        if r - l + 1 <= 10:
            insertion_sort(arr, l, r)
        else:
            mid = (l + r) // 2
            hybrid_sort(arr, l, mid)
            hybrid_sort(arr, mid + 1, r)
            merge(arr, l, mid, r)

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    hybrid_sort(arr, 0, n - 1)
    # write(" ".join(map(str, arr)) + "\n")

if __name__ == "__main__":
    main()