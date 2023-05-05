from collections import defaultdict
from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        remove_nums = defaultdict(int)

        if k >= len(nums) and len(nums) == 1:
            return (-1)
        elif k > len(nums):
            for i in range(len(nums)):
                remove_num = nums.pop(0)
                remove_nums[i] = remove_num
            remove_max = max(remove_nums.values())           
            return (remove_max)
        else:
            for i in range(k):
                remove_num = nums.pop(0)
                remove_nums[i] = remove_num
            remove_max = max(remove_nums.values())
            return remove_max