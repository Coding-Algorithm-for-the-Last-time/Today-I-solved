class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        def backtrack(i: int, subset: list[int]):
            if i >= len(nums):
                res.append(subset)
                return
            backtrack(i + 1, subset + [nums[i]])
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res
