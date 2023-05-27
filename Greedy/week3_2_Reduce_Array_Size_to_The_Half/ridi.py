from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for n in arr:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        l = list(d.values())
        l.sort(reverse=True)

        res = 0
        count = 0
        while count < len(arr) // 2:
            pop = l.pop(0)
            count += pop
            res += 1
        
        return res
    
    # Runtime 1798 ms Beats 5.14%
    # Memory 31.3 MB Beats 90.6%
    #TODO 리팩터링!


    def minSetSize_two(self, arr: List[int]) -> int:
        d = defaultdict(int)
        for n in arr:
            d[n] += 1
        
        heap = []
        for i in d.values():
            heapq.heappush(heap, (-1) * i)
    
        res = 0
        count = 0
        while count < len(arr) // 2:
            pop = heapq.heappop(heap)
            count += (-1) * pop
            res += 1
        
        return res
    
    # Runtime 631 ms Beats 39.65%
    # Memory 32.3 MB Beats 52.16%