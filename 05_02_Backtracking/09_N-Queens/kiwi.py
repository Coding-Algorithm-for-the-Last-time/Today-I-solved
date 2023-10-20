class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []

        def backtrack(i):
            if i == n:
                res.append(["".join(r) for r in board])
                return
            pos = set(range(n))
            for j in range(i):
                queen = board[j].index("Q")
                pos.discard(queen)
                pos.discard(queen - (i - j))
                pos.discard(queen + (i - j))
            for p in pos:
                board[i][p] = "Q"
                backtrack(i + 1)
                board[i][p] = "."

        backtrack(0)
        return res
