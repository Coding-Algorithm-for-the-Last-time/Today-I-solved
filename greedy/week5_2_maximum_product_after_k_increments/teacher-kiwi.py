import heapq


class Solution:
    def maximumProduct(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(k):
            heapq.heapreplace(nums, nums[0] + 1)
        for i in range(len(nums) - 1):
            nums[i + 1] = nums[i] * nums[i + 1] % (10**9 + 7)
        return nums[-1]
