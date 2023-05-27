class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        i, j = len(g) - 1, len(s) - 1
        while i > -1 and j > -1:
            if g[i] <= s[j]:
                j -= 1
            i -= 1
        return len(s) - j - 1


# Runtime 162 ms // Beats 78.85%
# Memory 15.8 MB // Beats 28.49%

############################################################################


class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort(reverse=True)
        s.sort()
        i = len(s) - 1
        for gf in g:
            if i < 0:
                break
            if gf <= s[i]:
                i -= 1
        return len(s) - i - 1


# Runtime 155 ms // Beats 95.14%
# Memory 15.9 MB // Beats 28.49%

############################################################################


class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        if len(s) == 0:
            return 0
        g.sort(reverse=True)
        s.sort()
        i = len(s) - 1
        for gf in g:
            if gf <= s[i]:
                i -= 1
                if i < 0:
                    break
        return len(s) - i - 1


# Runtime 173 ms // Beats 34.65%
# Memory 15.8 MB // Beats 73.85%
