from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        temp = 1
        zero_cnt = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_cnt += 1
            else:
                temp *= nums[i]

        if zero_cnt > 1:
            return [0] * len(nums)
        elif zero_cnt == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(temp)
                else:
                    res.append(0)
        else:
            for i in range(len(nums)):
                res.append(temp // nums[i])

        return res
