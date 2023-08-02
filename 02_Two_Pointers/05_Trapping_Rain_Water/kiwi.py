class Height:
    def __init__(self, l: int, r: int):
        self.l = l
        self.r = r


class Solution:
    def trap(self, height: list[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        w_height = Height(l=height[l], r=height[r])
        while l < r:
            if w_height.l > w_height.r:
                r -= 1
                res += max(0, w_height.r - height[r])
                w_height.r = max(w_height.r, height[r])
            else:
                l += 1
                res += max(0, w_height.l - height[l])
                w_height.l = max(w_height.l, height[l])
        return res
