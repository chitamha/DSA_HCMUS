import bisect

def main():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = list(map(int, input().split()))
    
    pivot = 0
    for i in range(0, n - 1):
        if arr[i + 1] < arr[i]:
            pivot = i

    for x in queries:
        id_st = bisect.bisect_left(arr, x, 0, pivot + 1)
        id_nd = bisect.bisect_left(arr, x, pivot + 1, n)
        if id_st < n and arr[id_st] == x:
            print(id_st)
        elif (id_nd < n and arr[id_nd] == x):
            print(id_nd)
        else:
            print(-1)
main()