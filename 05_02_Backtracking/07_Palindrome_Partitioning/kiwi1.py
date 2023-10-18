class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def is_palindrome(word):
            if len(word) == 1:
                return True
            e = len(word) - 1
            for s in range(len(word) // 2):
                if word[s] != word[e]:
                    return False
                e -= 1
            return True

        def backtrack(word, substrings: list[str]):
            if not word:
                res.append(substrings)
                return
            for i in range(1, len(word) + 1):
                if is_palindrome(word[:i]):
                    backtrack(word[i:], substrings + [word[:i]])

        backtrack(s, [])
        return res
