# https://leetcode.com/problems/first-missing-positive/


"""

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        a = [0] * 2**31

        for num in nums:
            if num > 0:
                a[num] = 1
        
        for i in range(1, len(a)):
            if a[i] == 0:
                return a[i]

>> MemoryError
    a = [0] * 2**31
"""

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        a = [0] * (len(nums) + 1)

        for num in nums:
            if num > 0 and num <= len(nums):
                a[num] = 1

        for i in range(1, len(a)):
            if a[i] == 0:
                return i
        
        return len(nums) + 1
