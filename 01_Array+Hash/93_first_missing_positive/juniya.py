class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        num_set = set(range(1, n+1))
        for num in nums:
            if num in num_set:
                num_set.remove(num)
        if len(num_set) == 0:
            return n+1
        else:
            return min(num_set)
        

