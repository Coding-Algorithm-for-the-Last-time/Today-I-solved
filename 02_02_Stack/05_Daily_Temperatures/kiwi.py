class Solution:
    def dailyTemperatures(self, t: list[int]) -> list[int]:
        stack = []
        res = [0] * len(t)
        for i in range(len(t) - 1, 0, -1):
            if t[i] > t[i - 1]:
                stack.append((i, t[i]))
                res[i - 1] = 1
            else:
                while stack and stack[-1][1] <= t[i - 1]:
                    stack.pop()
                res[i - 1] = 0 if not stack else stack[-1][0] - (i - 1)
        return res
