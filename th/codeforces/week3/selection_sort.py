import sys

def insertion_sort(n, arr):
    for i in range(n):
        idx = i
        for j in range(i + 1, n, 1):
            if arr[j] < arr[idx]:
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
        if idx != i:
            print(i, idx)

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    insertion_sort(n, arr)

main()