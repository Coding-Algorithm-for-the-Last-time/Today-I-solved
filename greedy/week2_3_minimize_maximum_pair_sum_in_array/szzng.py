# Runtime 1188 ms Beats 80.6%
# Memory 27.8 MB Beats 50.51%

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        half_len = len(nums)//2
        max_sum = 0

        for i in range(half_len):
            max_sum = max(max_sum, nums[i]+nums[-1*(i+1)])
        return max_sum
