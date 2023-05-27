from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = []
        for c in s:
            for i in range(len(l)):
                if c in l[i]:
                    l_left = l[:i]
                    l_right = l[i:]
                    new = ""
                    for string in l_right:
                        new += string
                    new += c
                    l = l_left.append(new)
                    break
            l.append(c)
        
        res = []
        for st in l:
            res.append(len(st))
        
        return res
