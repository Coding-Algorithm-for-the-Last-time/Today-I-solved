class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = prices[0]
        res = 0
        for price in prices:
            lowest = min(lowest, price)
            res = max(res, price - lowest)
        return res
