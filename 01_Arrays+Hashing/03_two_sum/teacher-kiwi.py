class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        while nums:
            num = nums.pop()
            other_num = target - num
            if other_num in nums:
                return [nums.index(other_num), len(nums)]