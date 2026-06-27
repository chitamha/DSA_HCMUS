import sys

class Solution:
    def solve(self, nums, k, n):
        def reloadNums(minIdx):
            nonlocal nums, n
            for i in range(minIdx, n - 1):
                nums[i] = nums[i + 1]

        ans = -1
        while k > 0:
            minIdx = 0
            for i in range(n):
                if nums[i] < nums[minIdx]:
                    minIdx = i
            ans = nums[minIdx]
            reloadNums(minIdx)
            n -= 1
            k -= 1

        return ans

    def findKthSmallest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        return self.solve(nums, k, n)

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().strip().split())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    ans = Solution()
    print(ans.findKthSmallest(nums, k))