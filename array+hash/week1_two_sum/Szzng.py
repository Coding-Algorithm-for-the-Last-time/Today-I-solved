from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        while len(nums) > 0:
            last_index = len(nums) - 1
            j = target - nums.pop()
            if j in nums:
                return [nums.index(j), last_index]
