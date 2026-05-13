import sys

def insertion_sort(n, arr):
    for i in range(n):
        j = i
        while j >= 1 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

def main():
    t = int(sys.stdin.readline())
    write = sys.stdout.write

    for query in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))

        insertion_sort(n, arr)

        count_del_ele = 0
        for i in range(n - 1):
            if arr[i + 1] - arr[i] <= 1:
                count_del_ele += 1
        
        if count_del_ele == n - 1:
            write(f"YES\n")
        else:
            write(f"NO\n")

if __name__ == "__main__":
    main()