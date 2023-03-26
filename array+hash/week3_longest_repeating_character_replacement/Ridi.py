# https://leetcode.com/problems/longest-repeating-character-replacement/


from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r, l = 0, 0
        m = defaultdict(int)
        res = 0
        while r < len(s):
            m[s[r]] += 1
            str_len = r - l + 1
            if str_len - max(m.values()) <= k:
                print(m)
                if str_len > res:
                    res = str_len
                    print(res)
            else:
                m[s[l]] -= 1
                l += 1
            r += 1
        return res


    def characterReplacement_two(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        # Optimization
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            # 추가된 dict 원소와 현재 최댓값 비교해 현재 최댓값 미리 계산
            maxf = max(maxf, count[s[r]])
            # maxf = 1

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
             