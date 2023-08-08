class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        a = 0
        for num in nums:
            a ^= num

        b = 0
        for i in range(len(nums) + 1):
            b ^= i

        return a ^ b
