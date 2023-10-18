class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def dfs(i: int, letter: str):
            if i >= len(digits):
                res.append(letter)
                return
            for char in letters[digits[i]]:
                dfs(i + 1, letter + char)

        if digits:
            dfs(0, "")
        return res
