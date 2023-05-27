from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        #TODO 길이 맞추기 작업 -> Szzng 풀이 참조

        res = 0
        while(len(s) != 0 and len(g) != 0 and max(s) >= min(g)):
            child = g[0]
            cookie = s[0]
            #TODO 효율성 올리기! -> 다른사람 풀이 참조.
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