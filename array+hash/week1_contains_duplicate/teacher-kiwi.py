class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return sorted(list(set(nums))) != sorted(nums)