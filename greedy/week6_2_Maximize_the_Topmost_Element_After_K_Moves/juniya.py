from collections import defaultdict
from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        remove_nums = defaultdict(int)

        if k % 2 != 0 and len(nums) == 1:
            return (-1)
        
        elif k > len(nums):
            for i in range(len(nums)):
                remove_num = nums.pop(0)
                remove_nums[i] = remove_num
            remove_max = max(remove_nums.values())           
            return (remove_max)
        
        elif k == len(nums):
            nums.pop(-1)
            return max(nums)
        else:
            if k == 1:
                remove_num = nums.pop(0)
                return nums[0]
            elif k >= 2 :
                remain_num = nums[k]
                for i in range(k-1):
                    remove_num= nums.pop(0)
                    remove_nums[i] = remove_num
                remove_max = max(remove_nums.values())
                return max(remain_num, remove_max)
            else:
                return nums[0]