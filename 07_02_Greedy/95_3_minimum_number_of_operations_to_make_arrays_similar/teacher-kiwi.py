class Solution:
    def makeSimilar(self, nums: list[int], target: list[int]) -> int:
        even_nums, odd_nums = [], []
        even_target, odd_target = [], []

        nums.sort()
        target.sort()
        for i in range(len(nums)):
            even_nums.append(nums[i]) if nums[i] % 2 == 0 else odd_nums.append(nums[i])
            even_target.append(target[i]) if target[i] % 2 == 0 else odd_target.append(
                target[i]
            )

        count = 0
        for i in range(len(even_nums)):
            count += abs(even_nums[i] - even_target[i])
        for i in range(len(odd_nums)):
            count += abs(odd_nums[i] - odd_target[i])

        return count // 4
