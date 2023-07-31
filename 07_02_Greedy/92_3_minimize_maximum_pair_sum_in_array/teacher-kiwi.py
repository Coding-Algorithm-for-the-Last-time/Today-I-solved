class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        res = 0
        i, j = 0, len(nums) - 1
        while i < j:
            res = max(res, nums[i] + nums[j])
            i, j = i + 1, j - 1
        return res


# Runtime 1206 ms // Beats 68.41%
# Memory 27.9 MB // Beats 50.51%

####################################################


class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        mid = len(nums) // 2
        return max(a + b for a, b in zip(nums[:mid], nums[: mid - 1 : -1]))


# Runtime 1110 ms // Beats 99.85%
# Memory 27.9 MB // Beats 27.22%
