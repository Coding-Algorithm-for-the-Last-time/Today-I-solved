class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def check(form, open, n):
            if open == 0 and n == 0:
                res.append(form)
            else:
                if open:
                    check(form + ")", open - 1, n)
                if n:
                    check(form + "(", open + 1, n - 1)

        check("(", 1, n - 1)

        return res
