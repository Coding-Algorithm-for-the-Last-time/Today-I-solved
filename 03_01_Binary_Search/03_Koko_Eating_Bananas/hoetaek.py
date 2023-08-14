import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        L = 1
        R = max(piles)
        res = R

        while L <= R:
            mid = (L + R) // 2

            mid_val = sum([math.ceil(i / mid) for i in piles])

            if mid_val <= h:
                res = min(res, mid)
                R = mid - 1
            else:
                L = mid + 1

        return res
