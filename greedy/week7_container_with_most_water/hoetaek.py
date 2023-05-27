from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        L = 0
        R = len(height) - 1

        while L < R:
            h = min(height[L], height[R])
            maxWater = max(maxWater, h * (R - L))

            if height[L] <= height[R]:
                L += 1
            else:
                R -= 1

        return maxWater
