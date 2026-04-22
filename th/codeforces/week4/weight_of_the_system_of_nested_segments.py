# import sys

# write = sys.stdout.write

# def quickSort(l, r, arr, category):
#     if l >= r:
#         return

#     pivot = arr[(l + r) // 2][category]
#     i, j = l, r
#     while True:
#         while arr[i][category] < pivot:
#             i += 1
#         while arr[j][category] > pivot:
#             j -= 1

#         if i >= j:
#             break

#         arr[i], arr[j] = arr[j], arr[i]
#         i, j = i + 1, j - 1
    
#     quickSort(l, j, arr, category)
#     quickSort(j + 1, r, arr, category)

# def process(n, m, points):
#     quickSort(0, m - 1, points, 1)

#     sumOfWeights = 0
#     for i in range(2*n):
#         sumOfWeights += points[i][1]
#     write(f"{sumOfWeights}\n")

#     quickSort(0, 2*n - 1, points, 0)
#     for i in range(n):
#         write(f"{points[i][2] + 1} {points[2*n - i - 1][2] + 1}\n")

# def main():
#     t = int(sys.stdin.readline())
#     for query in range(t):
#         sys.stdin.readline()
#         n, m = map(int, sys.stdin.readline().split())

#         points = []
#         for i in range(m):
#             coordinate, weight = map(int, sys.stdin.readline().split())
#             points.append((coordinate, weight, i))
        
#         process(n, m, points)
#         write(f"\n")

# if __name__ == "__main__":
#     main()

import sys

write = sys.stdout.write

def process(n, m, points):
    points.sort(key = lambda x : x[1])

    sumOfWeights = 0
    for i in range(2*n):
        sumOfWeights += points[i][1]
    write(f"{sumOfWeights}\n")

    points[ : 2*n] = sorted(points[ : 2*n], key = lambda x : x[0])
    for i in range(n):
        write(f"{points[i][2] + 1} {points[2*n - i - 1][2] + 1}\n")

def main():
    t = int(sys.stdin.readline())
    for query in range(t):
        sys.stdin.readline()
        n, m = map(int, sys.stdin.readline().split())

        points = []
        for i in range(m):
            coordinate, weight = map(int, sys.stdin.readline().split())
            points.append((coordinate, weight, i))
        
        process(n, m, points)
        write(f"\n")

if __name__ == "__main__":
    main()