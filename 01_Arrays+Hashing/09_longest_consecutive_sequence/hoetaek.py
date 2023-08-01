from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(sorted(set(nums)))
        max_l = 1
        length = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                length += 1
            else:
                length = 1
            max_l = max(max_l, length)
        return max_l
