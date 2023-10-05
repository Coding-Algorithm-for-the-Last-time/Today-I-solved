class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(i, memo: list):
            res.append(memo)
            for j in range(i, len(nums)):
                dfs(j + 1, memo + [nums[j]])

        dfs(0, [])
        return res
