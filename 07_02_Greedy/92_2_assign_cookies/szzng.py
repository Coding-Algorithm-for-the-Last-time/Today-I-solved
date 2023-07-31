# Runtime 147 ms Beats 99.78%
# Memory 15.5 MB Beats 99.15%


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort()
        end = min(len(s), len(g))
        if len(g) > end: g = g[-1 * end:]
        if len(s) > end: s = s[-1 * end:]
        result = 0

        for i in g:
            if len(s) == 0:
                return result

            if s[-1] >= i:
                result += 1
                s.pop()

        return result
