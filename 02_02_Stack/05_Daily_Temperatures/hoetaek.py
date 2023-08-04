class Solution:
    def dailyTemperatures(self, t: list[int]) -> list[int]:
        stack = []
        res = [0] * len(t)

        for i in range(len(t) - 1, 0, -1):
            if t[i] > t[i - 1]:
                # 내리막길
                res[i - 1] = 1
                stack.append((i, t[i]))
            else:
                # 오르막길
                if stack:
                    while stack and stack[-1][1] <= t[i - 1]:
                        stack.pop()
                    res[i - 1] = stack[-1][0] - i + 1

        return res
