import sys

write = sys.stdout.write

def quick_sort(l, r, arr):
    if l >= r:
        return

    p_idx = l
    pivot = arr[p_idx]
    i, j = l, r

    while True:
        while arr[i] < pivot:
            write(f"{min(i, p_idx)} {max(i, p_idx)}\n")
            i += 1
        write(f"{min(i, p_idx)} {max(i, p_idx)}\n")

        while arr[j] > pivot:
            write(f"{min(j, p_idx)} {max(j, p_idx)}\n")
            j -= 1
        write(f"{min(j, p_idx)} {max(j, p_idx)}\n")

        # Khi hai con trỏ chạm hoặc vượt nhau thì dừng phân hoạch
        if i >= j:
            break
            
        arr[i], arr[j] = arr[j], arr[i]
        i, j = i + 1, j - 1
    
    # print(arr)

    quick_sort(l, j, arr)
    quick_sort(j + 1, r, arr)

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    quick_sort(0, n-1, arr)
    
    # write(f"{' '.join([str(x) for x in arr])}")

if __name__ == "__main__":
    main()