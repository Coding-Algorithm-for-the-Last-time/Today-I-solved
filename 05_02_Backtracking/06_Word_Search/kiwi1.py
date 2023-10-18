class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])

        def backtrack(r: int, c: int, i: int, visit: list):
            if (
                r < 0
                or r >= ROW
                or c < 0
                or c >= COL
                or board[r][c] != word[i]
                or (r, c) in visit
                or len(visit) >= len(word)
            ):
                return False

            if len(visit) + 1 == len(word) and board[r][c] == word[i]:
                return True

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if backtrack(r + dr, c + dc, i + 1, visit + [(r, c)]):
                    return True
            return False

        for r in range(ROW):
            for c in range(COL):
                if backtrack(r, c, 0, []):
                    return True
        return False
