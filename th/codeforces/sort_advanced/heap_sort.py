import sys

write = sys.stdout.write

# Thao tác Sift-down (vun đống)
def siftDown(i, heapSize, arr):
    while True:
        largest = i
        left, right = 2*i + 1, 2*i + 2

        if left < heapSize:
            write(f"{left} {largest}\n")
            if arr[left] > arr[largest]:
                largest = left
        
        if right < heapSize:
            write(f"{right} {largest}\n")
            if arr[right] > arr[largest]:
                largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest
        else:
            break

def solve(n, arr):
    # Giai đoạn 1: Build Max-Heap
    for i in range(n//2 - 1, -1, -1):
        siftDown(i, n, arr)
    
    # Giai đoạn 2: Sắp xếp
    for i in range(n - 1, 0, -1):
        # Đưa phần tử lớn nhất hiện tại về cuối mảng
        arr[0], arr[i] = arr[i], arr[0]
        # Vun đống lại phần tử vừa đưa lên đỉnh
        siftDown(0, i, arr)

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    solve(n, arr)

if __name__ == '__main__':
    main()