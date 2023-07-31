class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        res = 0
        for i in range(len(cost)):
            if i % 3 != 2:
                res += cost[i]
        return res


# Runtime 45 ms // Beats 71.96%
# Memory 13.8 MB // Beats 45.57%

###################################################


class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        cost.sort(reverse=True)
        for i in range(1, len(cost)):
            cost[i] = cost[i] + cost[i - 1] if i % 3 != 2 else cost[i - 1]
        return cost[-1]


# Runtime 49 ms // Beats 47.63%
# Memory 13.9 MB // Beats 45.57%
