class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = float("inf")
        while l <= r:
            c = (l + r) // 2
            minimum = min(minimum, nums[c])
            if nums[c] > nums[r]:
                l = c + 1
            else:
                r = c - 1
        return minimum
