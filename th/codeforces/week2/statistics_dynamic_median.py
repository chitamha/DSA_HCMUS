import sys
import bisect

def insertion_sort(val, arr):
    idx = bisect.bisect_left(arr, val)
    arr.insert(idx, val)

def main():
    n = int(sys.stdin.readline().strip())
    arr = []
    for x in sys.stdin.readline().split():
        insertion_sort(int(x), arr)
        if len(arr) % 2 != 0:
            print(arr[len(arr) // 2])
        else:
            if (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) % 2 == 0:
                print((arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) // 2)
            else:
                print((arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) / 2)

main()