import sys

def merge(l, mid, r, arr, aux):
    i, j, k = l, mid + 1, l
    while i <= mid and j <= r:
        if arr[i][0] <= arr[j][0]:
            aux[k] = arr[i]
            k += 1
            i += 1
        else:
            aux[k] = arr[j]
            k += 1
            j += 1
    
    while i <= mid:
        aux[k] = arr[i]
        k += 1
        i += 1
    
    while j <= r:
        aux[k] = arr[j]
        k += 1
        j += 1
    
    for idx in range(l, r + 1):
        arr[idx] = aux[idx]

def mergeSort(l, r, arr, aux):
    if l >= r:
        return
    
    mid = (l + r) // 2
    mergeSort(l, mid, arr, aux)
    mergeSort(mid + 1, r, arr, aux)
    merge(l, mid, r, arr, aux)

def main():
    n = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))
    frontColor = list(map(int, sys.stdin.readline().split()))
    backColor = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    favouriteColors = list(map(int, sys.stdin.readline().split()))

    tShirts = []
    for i in range(n):
        tShirts.append((prices[i], frontColor[i], backColor[i]))

    aux = [(0, 0, 0)] * n
    mergeSort(0, n - 1, tShirts, aux)

    for i in range(m):
        j, flag = 0, 0
        while j < len(tShirts):
            if favouriteColors[i] == tShirts[j][1] or favouriteColors[i] == tShirts[j][2]:
                print(tShirts[j][0], end = " ")
                del tShirts[j]
                flag = 1
                break
            j += 1

        if flag == 0:
            print(-1, end = " ")
        
main()