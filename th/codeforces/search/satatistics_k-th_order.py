def count(arr, val):
    cnt = 0
    for i in range(len(arr)):
        if arr[i] <= val:
            cnt += 1
    return cnt 

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    l, r = int(-1e9), int(1e9)
    while (l <= r):
        mid = (l + r) // 2
        if count(arr, mid) >= k:
            r = mid - 1
        else:
            l = mid + 1
    
    print(r + 1)

main()