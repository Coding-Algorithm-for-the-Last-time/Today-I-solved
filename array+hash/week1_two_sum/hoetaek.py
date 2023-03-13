from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        for i in range(len(nums)):
            if target - nums[i] in hs:
                return [hs[target - nums[i]], i]
            else:
                hs[nums[i]] = i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]