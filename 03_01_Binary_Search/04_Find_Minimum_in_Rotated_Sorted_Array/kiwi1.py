class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            c = (l + r) // 2
            if nums[c] == min(nums[l], nums[c], nums[r]):
                if c != 0 and nums[c - 1] > nums[c]:
                    return nums[c]
                r = c - 1
            elif nums[c] == max(nums[l], nums[c], nums[r]):
                l = c + 1
            else:
                return nums[l]
        return nums[c]
