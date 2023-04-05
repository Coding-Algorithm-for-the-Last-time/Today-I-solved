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
