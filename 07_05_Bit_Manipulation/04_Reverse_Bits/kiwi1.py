class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if n & (2**i) == 2**i:
                res += 2 ** (31 - i)
        return res
