import bisect

def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = list(map(int, input().split()))

    arr.sort()

    for x in queries:
        id = bisect.bisect_left(arr, x)
        if id - 1 >= 0 and id < n:
            if arr[id] - x <= x - arr[id - 1]:
                print(arr[id])
            else:
                print(arr[id - 1])
        elif (id - 1 < 0):
            print(arr[id])
        else:
            print(arr[id - 1])

main()