from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        b_dict = {")": "(", "}": "{", "]": "["}
        for bracket in s:
            if stack and b_dict.get(bracket) == stack[-1]:
                stack.pop()
            else:
                stack.append(bracket)
        return True if not stack else False
