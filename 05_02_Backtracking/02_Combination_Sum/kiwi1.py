class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def minus(i, target, combination: list):
            if candidates[i] > target:
                return
            combination.append(candidates[i])
            if candidates[i] == target:
                res.append(combination)
                return
            target -= candidates[i]
            for j in range(i, len(candidates)):
                copied_target = target
                copied_combination = [*combination]
                minus(j, copied_target, copied_combination)

        for i in range(len(candidates)):
            minus(i, target, [])
        return res
