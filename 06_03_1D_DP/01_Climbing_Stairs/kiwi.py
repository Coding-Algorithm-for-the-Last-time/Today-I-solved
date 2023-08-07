class Solution:
    def climbStairs(self, n: int) -> int:
        curr, prev = 1, 1
        for i in range(2, n + 1):
            curr, prev = curr + prev, curr
        return curr
