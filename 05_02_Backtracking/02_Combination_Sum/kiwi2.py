class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dfs(i, target, combination: list):
            if i >= len(candidates) or target < 2:
                return
            if candidates[i] == target:
                res.append(combination + [candidates[i]])
            dfs(i, target - candidates[i], combination + [candidates[i]])
            dfs(i + 1, target, combination)

        dfs(0, target, [])
        return res
