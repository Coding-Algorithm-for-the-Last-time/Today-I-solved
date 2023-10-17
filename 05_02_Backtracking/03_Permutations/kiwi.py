class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def dfs(i: int, permutation: list[int]):
            if nums[i] in permutation:
                return
            if len(permutation + [nums[i]]) == len(nums):
                res.append(permutation + [nums[i]])
                return
            for j in range(len(nums)):
                dfs(j, permutation + [nums[i]])

        for i in range(len(nums)):
            dfs(i, [])

        return res
