from typing import List
import heapq

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        # O(N logN)
        nums.sort()


        # O(K)
        while k > 0 :
            if len(nums) == 1:
                return nums[0] + k

            # O(N)
            idx = 0
            while idx < len(nums) - 2 and nums[idx] == nums[idx + 1]:
                idx += 1
            
            if nums[idx] != nums[idx + 1]:
                nums[idx] += 1   
            else:
                if idx == len(nums) - 2:
                    nums[idx + 1] += 1
                else:
                    nums[idx] += 1

            k -= 1
        
        # O(N logN + K N)
        res = 1
        for i in nums:
            res *= i
        
        # O(N logN + (K+1) N)
        return res % (10**9 + 7)

    # Time Limit Exceeded

    def maximumProduct_queue(self, nums: List[int], k: int) -> int:
        h = nums[:]
        # O(N)
        heapq.heapify(nums)

        # O(k)
        for _ in range(k):
            # O(log N)
            minimum = heapq.heappop(h)
            heapq.heappush(h, minimum + 1)
        
        # O(K log N + N )
        MOD = 10**9 + 7
        res = 1
        for i in h:
            res *= i
            res % MOD
        
        # O(K log N + 2 N)
        return res
    
    # reference : https://youtu.be/lSr-tKjbiAM