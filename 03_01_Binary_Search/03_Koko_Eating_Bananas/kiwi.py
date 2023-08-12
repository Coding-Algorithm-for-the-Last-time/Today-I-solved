class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            c = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += -(-pile // c)
            if hours > h:
                l = c + 1
            elif hours <= h:
                r = c - 1
        return c + 1 if h < hours else c
