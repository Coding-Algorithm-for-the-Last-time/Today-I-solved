class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = set()
        t = 0
        nums.sort()
        while t < len(nums) and nums[t] < 1:
            l, r = t + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < -nums[t]:
                    l += 1
                elif nums[l] + nums[r] > -nums[t]:
                    r -= 1
                else:
                    res.add((nums[t], nums[l], nums[r]))
                    l, r = l + 1, r - 1
            t += 1
        return res
