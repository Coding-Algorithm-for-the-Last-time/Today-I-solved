class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res, memo = [[]], set()

        def dfs(nums):
            if not nums:
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1 :])
            if str(nums) not in memo:
                memo.add(str(nums))
                res.append(nums)

        dfs(nums)
        return res
