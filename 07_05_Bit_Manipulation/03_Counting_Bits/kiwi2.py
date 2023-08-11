class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            res[i] = res[i - offset] + 1
        return res
