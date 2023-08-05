class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_s = set()
        res = 0
        left = 0
        for right in range(len(s)):
            while s[right] in sub_s:
                sub_s.remove(s[left])
                left += 1
            sub_s.add(s[right])
            res = max(res, right - left + 1)
        return res
