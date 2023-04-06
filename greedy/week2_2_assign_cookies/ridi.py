from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        res = 0
        while(len(s) != 0 and len(g) != 0 and max(s) >= min(g)):
            child = g[0]
            cookie = s[0]
            if cookie >= child:
                res += 1
                g.pop(0)
                s.pop(0)
                i = 0
                continue
            s.pop(0)
        
        return res

    # Very Very Bad... Runtime Beats 5.2% / Memory Beats 96.28%
                        #4559 ms          /  15.5 MB