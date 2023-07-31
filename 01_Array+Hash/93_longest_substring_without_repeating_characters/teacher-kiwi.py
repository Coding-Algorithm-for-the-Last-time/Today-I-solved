from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = deque()
        data = {}
        result = 0
        for char in s:
            while char in data:
                data.pop(substring.popleft())
            substring.append(char)
            data[char] = 1
            result = max(len(data), result)
        return result