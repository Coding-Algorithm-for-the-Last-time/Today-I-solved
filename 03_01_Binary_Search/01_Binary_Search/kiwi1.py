class Solution:
    def search(self, nums: list[int], target: int) -> int:
        s, e = 0, len(nums) - 1
        res = -1

        while s + 1 < e:
            i = (s + e) // 2
            if nums[i] == target:
                res = i
                break
            if nums[i] > target:
                e = i
            else:
                s = i

        return s if nums[s] == target else e if nums[e] == target else res
