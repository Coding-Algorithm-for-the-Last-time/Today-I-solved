class Solution:
    def trap(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        l_high = height[0]
        r_high = height[-1]
        trapped = 0
        while l < r:
            if l_high < r_high:
                l += 1
                l_high = max(l_high, height[l])
                trapped += l_high - height[l]
            else:
                r -= 1
                r_high = max(r_high, height[r])
                trapped += r_high - height[r]
        return trapped
