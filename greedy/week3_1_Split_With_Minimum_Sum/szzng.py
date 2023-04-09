# Runtime 27 ms Beats 88.73%
# Memory 13.8 MB Beats 94.20%


class Solution:
    def splitNum(self, num: int) -> int:
        num = sorted(list(str(num)))
        a = b = ''

        for i in range(0, len(num), 2): a += num[i]
        for i in range(1, len(num), 2): b += num[i]

        return int(a) + int(b)
