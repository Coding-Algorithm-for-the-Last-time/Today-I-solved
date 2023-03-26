# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(s)
        res = 0
        l = 0
        sub = list()

        for r in range(len(s)):
                        
            if s[r] not in sub:
                sub.append(s[r])
                if len(sub) > res:
                    res = len(sub)
                r += 1
            else:
                sub.pop(0)
                l += 1 
        return res


    def lengthOfLongestSubstring_two(self, s: str) -> int:
        sub = set()
        res = 0

        l = 0
        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1

            sub.add(s[r])
            res = max(res, r - l + 1)

        return res