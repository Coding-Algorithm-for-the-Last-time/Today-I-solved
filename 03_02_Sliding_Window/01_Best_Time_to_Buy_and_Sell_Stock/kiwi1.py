class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        gaps = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
        sums = [0] * (len(gaps) + 1)

        if not gaps:
            return 0

        sums[0] = gaps[0]
        for i in range(1, len(gaps)):
            sums[i] = max(sums[i - 1] + gaps[i], gaps[i])
        return max(sums)
