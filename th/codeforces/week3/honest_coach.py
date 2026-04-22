import sys

def bubble_sort(n, arr):
    for i in range(n):
        j = 0
        while j + 1 < n - i:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1

    # print(arr)

def main():
    t = int(sys.stdin.readline())
    write = sys.stdout.write

    for query in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))

        bubble_sort(n, arr)
        ans = arr[n - 1]
        for i in range(n - 1):
            ans = min(ans, arr[i + 1] - arr[i])
        
        write(f"{ans}\n")
    
if __name__ == "__main__":
    main()