# Runtime 42 ms Beats 85.15%
# Memory 13.8 MB Beats 45.57%

from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        result = 0
        for i in range(len(cost)):
            if i % 3 == 2:
                continue
            result += cost[i]
        return result
