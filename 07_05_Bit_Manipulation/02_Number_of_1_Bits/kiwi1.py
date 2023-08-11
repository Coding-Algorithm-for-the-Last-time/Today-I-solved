class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for i in range(31, -1, -1):
            if n & (2**i) == 2**i:
                cnt += 1
        return cnt
