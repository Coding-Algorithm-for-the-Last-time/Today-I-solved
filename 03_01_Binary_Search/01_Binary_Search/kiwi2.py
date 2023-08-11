class Solution:
    def search(self, nums: list[int], target: int) -> int:
        s, e = 0, len(nums) - 1
        while s < e:
            i = s + (e - s) // 2
            if nums[i] == target:
                return i
            if nums[i] > target:
                e = i - 1
            else:
                s = i + 1
        return s if nums[s] == target else e if nums[e] == target else -1
