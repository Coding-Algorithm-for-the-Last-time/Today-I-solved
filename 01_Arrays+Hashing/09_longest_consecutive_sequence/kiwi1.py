from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(list(set(nums)))
        prev = nums[0]
        res = [1, 0]
        for num in sorted(nums):
            if prev + 1 == num:
                res[0] += 1
                prev += 1
            else:
                res[1] = max(res)
                res[0] = 1
                prev = num
        return max(res)
