class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        increments = 0
        target = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < target + 1:
                increments += target + 1 - nums[i]
            target = max(target + 1, nums[i])

        return increments