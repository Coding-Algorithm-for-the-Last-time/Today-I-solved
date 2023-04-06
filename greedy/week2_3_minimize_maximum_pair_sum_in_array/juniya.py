class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_pair_sum = 0
        
        for i in range(n//2):
            max_pair_sum = max(max_pair_sum, (nums[i]+nums[n-i-1])) 
        return max_pair_sum
    
#Runtime 1247ms Beats 37.99% Memory 27.6MB Beats 86.61%