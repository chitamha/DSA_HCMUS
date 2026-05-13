import sys

def insertion_sort(n, arr):
    write = sys.stdout.write

    for i in range (n):
        j = i
        while j >= 1 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            write(f"{j - 1} {j}\n")
            j -= 1

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    insertion_sort(n, arr)

if __name__ == "__main__":
    main()