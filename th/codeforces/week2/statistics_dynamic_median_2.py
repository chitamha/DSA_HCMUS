import sys
import heapq

def main():
    def import_stream():
        for line in sys.stdin:
            for x in line.split():
                yield int(x)

    stream = import_stream()
    n = next(stream)

    left_max_heap = []
    right_min_heap = []

    for i in range(1, n + 1, 1):
        x = next(stream)

        heapq.heappush(left_max_heap, -x)
        ## Khi them nhu nay, co the x lon hon phan tu nho nhat cua right_min_heap
        ## nen ta push phan tu dau left_max_heap vao right_min_heap
        heapq.heappush(right_min_heap, -heapq.heappop(left_max_heap))
        if len(left_max_heap) < len(right_min_heap):
            heapq.heappush(left_max_heap, -heapq.heappop(right_min_heap))

        if i % 2 == 0:
            if (left_max_heap[0] + right_min_heap[0]) % 2 == 0:
                print((-left_max_heap[0] + right_min_heap[0]) // 2)
            else:
                print((-left_max_heap[0] + right_min_heap[0]) / 2)
        else:
            print(-left_max_heap[0])
main()