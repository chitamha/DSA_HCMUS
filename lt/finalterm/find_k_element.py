import sys

class Solution:
    def partition(self, arr, low, high):
        i, j = low - 1, high + 1
        pivotIdx = (i + j) // 2
        pivot = arr[pivotIdx]
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1

            if i >= j:
                return j
            
            arr[i], arr[j] = arr[j], arr[i]


    def solve(self, n, k, low, high, arr):
        if low == high:
            return arr[low]
            
        j = self.partition(arr, low, high)
        left_count = j - low + 1
        
        if k <= left_count:
            # Hoare's partition includes j in the left half, so we recurse on [low...j]
            return self.solve(n, k, low, j, arr)
        else:
            return self.solve(n, k - left_count, j + 1, high, arr)

    def findKthSmallest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        return self.solve(n, k, 0, n - 1, nums)

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    ans = Solution()
    print(ans.findKthSmallest(arr, k))
