class Solution:
    def minimumSum(self, num: int) -> int:
        nums = list(str(num))
        nums = sorted(nums)
        return int(nums[0]+nums[3]) +int(nums[1]+nums[2])
