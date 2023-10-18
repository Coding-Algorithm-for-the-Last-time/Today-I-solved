class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        substring = []

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def backtrack(i):
            if i >= len(s):
                res.append(substring[:])
                return
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    substring.append(s[i : j + 1])
                    backtrack(j + 1)
                    substring.pop()

        backtrack(0)
        return res
