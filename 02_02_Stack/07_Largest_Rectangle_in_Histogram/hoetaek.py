class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        monostack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while monostack and monostack[-1][1] > h:
                index, height = monostack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index

            monostack.append((start, h))

        for i, h in monostack:
            area = h * (len(heights) - i)
            maxArea = max(maxArea, area)

        return maxArea
