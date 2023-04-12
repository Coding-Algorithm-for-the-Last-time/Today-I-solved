from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        cur_max = 0

        #TODO looping n // 2 만큼
        for i in range(n):
            s = nums[i] + nums[n - 1 - i]
            if s > cur_max:
                cur_max = s

        return cur_max        
