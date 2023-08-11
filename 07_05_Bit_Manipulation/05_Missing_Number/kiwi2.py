class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)
        for i in range(res):
            res += i - nums[i]
        return res
