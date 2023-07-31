class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        g.sort()
        s.sort()
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i+=1
            j+=1

        return res


#Runtime 172 ms Beats 38.98% , Memory 15.8 MB Beats 28.99%