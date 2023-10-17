class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        def backtrack(i: int, subset: list[int]):
            if (sum_subset := sum(subset)) == target:
                res.append(subset)
                return
            if i >= len(candidates) or sum_subset > target:
                return
            backtrack(i + 1, subset + [candidates[i]])
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res
