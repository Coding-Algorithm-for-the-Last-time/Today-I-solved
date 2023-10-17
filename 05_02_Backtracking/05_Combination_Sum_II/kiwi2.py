class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(i: int, subset: list[int], target: int):
            if i >= len(candidates) or candidates[i] > target:
                return
            if candidates[i] == target:
                res.append(subset + [candidates[i]])
                return
            backtrack(i + 1, subset + [candidates[i]], target - candidates[i])
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, subset, target)

        backtrack(0, [], target)
        return res
