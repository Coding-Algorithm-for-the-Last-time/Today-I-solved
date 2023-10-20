class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0
        for i in range(1, len(nums)):
            temp = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = temp
        res1 = rob2

        rob1, rob2 = 0, 0
        for i in range(len(nums) - 1):
            temp = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = temp
        res2 = rob2

        return max(nums[0], res1, res2)
