class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        for i in range(len(s)):
            for l, r in [(i, i), (i, i + 1)]:
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    temp = (l, r)
                    l -= 1
                    r += 1
                if temp[1] - temp[0] > right - left:
                    left, right = temp
        return s[left : right + 1]
