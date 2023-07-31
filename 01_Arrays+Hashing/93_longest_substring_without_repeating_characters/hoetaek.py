class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        hs = set()
        max_length = 0
        for R in range(len(s)):
            while s[R] in hs and L < R:
                hs.remove(s[L])
                L += 1
                
            max_length = max(max_length, R - L + 1)
            hs.add(s[R])
            
        return max_length