class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        while k:
            heappush(nums, heappop(nums)+1)
            k-=1
        
        res = 1
        modulo  = 10**9+7
        for n in nums:
            res = (res*n)%modulo

        return res
