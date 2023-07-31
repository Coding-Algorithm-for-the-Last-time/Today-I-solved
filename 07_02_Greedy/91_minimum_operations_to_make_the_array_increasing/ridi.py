class Solution:
    def minOperations(self, nums: list[int]) -> int:
        res = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                continue
            else:
                diff = nums[i] - nums[i+1] + 1
                nums[i + 1] += diff
                res += diff
        return res
    # too slow!! -> Runtime Beats 23.88%

    def minOperations_fast(self, nums: list[int]) -> int:
        res = 0

        prev = nums[0]
        for i in range(1, len(nums)):
            now = nums[i]
            if prev < now:
                prev = now
                continue
            else:
                diff = prev - now + 1
                prev = now + diff
                res += diff

        return res
    # not bad:) -> Runtime Beats 92.72%