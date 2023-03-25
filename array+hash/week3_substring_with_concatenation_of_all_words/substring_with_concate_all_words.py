# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

import copy

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        unit_len = len(words[0])
        total_len = len(words) * unit_len
        res = []

        for i in range(len(s) - total_len + 1):
            # print(f"i: {i}")
            start = i
            words_dup = copy.deepcopy(words)
            # print(words)
            # print(words_dup)

            for j in range(start, start + total_len, unit_len):
                # print(f"j: {j}")
                sub = s[j:j+unit_len]
                if sub in words_dup:
                    words_dup.remove(sub)
                else:
                    break
            if len(words_dup) == 0:
                res.append(start)
            
            # print(words_dup)
            # print("-"*20)
        
        return res
