import sys

def findKMax(n, k, arr):
    for i in range(k):
        j = 0
        while j + 1 < n:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1

    return arr[n - k : n]

def findKMin(n, k, arr):
    for i in range(k):
        j = n - 1
        while j - 1 >= 0:
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    return arr[0 : k]

def main():
    t = int(sys.stdin.readline())
    write = sys.stdout.write

    for query in range(t):
        n, k = map(int, sys.stdin.readline().split())
        arr_st = list(map(int, sys.stdin.readline().split()))
        arr_nd = list(map(int, sys.stdin.readline().split()))
        
        sub_arr_st = findKMin(n, k, arr_st)
        sub_arr_nd = findKMax(n, k, arr_nd)
        sub_arr = sub_arr_st + sub_arr_nd

        sub_arr.sort()

        ans = sum(arr_st[:]) - sum(sub_arr_st[:]) + sum(sub_arr[-k : ])
        write(f"{ans}\n")

if __name__ == "__main__":
    main()