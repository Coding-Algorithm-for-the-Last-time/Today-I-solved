class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = [(target - p) / s for p, s in sorted(zip(position, speed))]
        res, temp = 0, 0
        while stack:
            t = stack.pop()
            if t > temp:
                temp = t
                res += 1
        return res
