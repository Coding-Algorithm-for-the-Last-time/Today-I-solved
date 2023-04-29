from typing import List
import math


class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        
        nums_odd = []
        nums_even = []
        
        target_odd = []
        target_even = []

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums_even.append(nums[i])
            else:
                nums_odd.append(nums[i])
            
            if target[i] % 2 == 0:
                target_even.append(target[i])
            else:
                target_odd.append(target[i])

        nums_odd.sort()
        nums_even.sort()
        
        target_odd.sort()
        target_even.sort()

        entrophy = sum([abs(nums_odd[i] - target_odd[i]) for i in range(len(nums_odd))])
        entrophy += sum([abs(nums_even[i] - target_even[i]) for i in range(len(nums_even))])

        return math.ceil(entrophy / 4)