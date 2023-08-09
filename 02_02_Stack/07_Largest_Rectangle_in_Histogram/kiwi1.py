class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [[0, 1]]
        largest = 0

        for h in heights:
            if h == stack[-1][0]:
                stack[-1][1] += 1
            else:
                width = 0
                while h < stack[-1][0]:
                    rect = stack.pop()
                    largest = max(largest, rect[0] * (rect[1] + width))
                    width += rect[1]
                stack.append([h, width + 1])
        width = 0
        while stack:
            rect = stack.pop()
            largest = max(largest, rect[0] * (rect[1] + width))
            width += rect[1]

        return largest
