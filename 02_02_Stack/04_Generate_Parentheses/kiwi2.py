class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = []

        def backtrack(opened: int, closed: int) -> None:
            if opened == closed == n:
                res.append("".join(stack))
            else:
                if n > opened:
                    stack.append("(")
                    backtrack(opened + 1, closed)
                    stack.pop()
                if opened > closed:
                    stack.append(")")
                    backtrack(opened, closed + 1)
                    stack.pop()

        backtrack(0, 0)
        return res
