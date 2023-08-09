class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # [index, height]
        largest = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                largest = max(largest, height * (i - index))
                start = index
            stack.append([start, h])

        for i, h in stack:
            largest = max(largest, h * (len(heights) - i))
        return largest
