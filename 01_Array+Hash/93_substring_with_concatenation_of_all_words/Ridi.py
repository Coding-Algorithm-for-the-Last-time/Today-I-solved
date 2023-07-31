# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

import copy

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        unit_len = len(words[0])
        total_len = len(words) * unit_len
        res = []

        for i in range(len(s) - total_len + 1):
            start = i
            words_dup = copy.deepcopy(words)

            for j in range(start, start + total_len, unit_len):
                sub = s[j:j+unit_len]
                if sub in words_dup:
                    words_dup.remove(sub)
                else:
                    break
            if len(words_dup) == 0:
                res.append(start)
        
        return res
