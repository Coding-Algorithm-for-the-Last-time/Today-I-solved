from functools import reduce


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        cnt, order = {}, []
        for i in range(len(s)):
            if s[i] in cnt:
                cnt[s[i]][1] = i
            else:
                cnt[s[i]] = [i, i]
                order.append(s[i])

        res = []

        def reduce_func(acc, c):
            if acc[1] + 1 == cnt[c][0]:
                res.append(cnt[c][0] - acc[0])
                return cnt[c]
            return [acc[0], max(acc[1], cnt[c][1])]

        a, b = reduce(reduce_func, order, [0, 0])

        return res + [b - a + 1]


# Runtime 40 ms // Beats 70.96%
# Memory 13.8 MB // Beats 55.91%

####################################################
# 설탕 쌤 코드 참고


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt, order = {}, []
        for i in range(len(s)):
            if s[i] in cnt:
                cnt[s[i]][1] = i
            else:
                cnt[s[i]] = [i, i]
                order.append(s[i])

        res = []
        l, r = 0, 0
        for c in order:
            if r + 1 == cnt[c][0]:
                res.append(r - l + 1)
                l = r + 1
            r = max(r, cnt[c][1])

        return res + [r - l + 1]


# Runtime 39 ms // Beats 76.11%
# Memory 13.9 MB // Beats 55.91%
