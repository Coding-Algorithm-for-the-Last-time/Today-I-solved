from heapq import heappush, heappop

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        heap = []
        data = {}
        for num in nums:
            if num > 0 and num not in data:
                heappush(heap, num)
                data[num] = 1
        result = 0
        while heap and heappop(heap) == result + 1 :
            result += 1
        return result + 1
    
##############################################################

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        nums.sort()
        result = 0
        for num in nums:
            if num > result + 1:
                return result + 1
            if num == result + 1:
                result += 1
        return result + 1