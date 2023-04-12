from typing import List

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
        
