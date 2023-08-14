class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            c = l + (r - l) // 2
            if nums[c] == target:
                return c
            if nums[c] < nums[r]:
                if target < nums[c] or target > nums[r]:
                    r = c - 1
                else:
                    l = c + 1
            else:
                if target > nums[c] or target < nums[l]:
                    l = c + 1
                else:
                    r = c - 1
        return -1
