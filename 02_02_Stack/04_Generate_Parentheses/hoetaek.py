class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def getParenthesis(parenthesis, flag):
            if len(parenthesis) == n * 2:
                if flag == 0:
                    res.append(parenthesis)
                return

            if flag < 0:
                return

            getParenthesis(parenthesis + "(", flag + 1)
            getParenthesis(parenthesis + ")", flag - 1)

        getParenthesis("", 0)

        return res
