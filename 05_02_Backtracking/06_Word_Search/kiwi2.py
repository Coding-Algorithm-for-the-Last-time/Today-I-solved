from collections import Counter


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        if len(word) > len(board) * len(board[0]):
            return False

        count = Counter(sum(board, []))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        ROW, COL = len(board), len(board[0])
        visit = set()

        def backtrack(r: int, c: int, i: int):
            if (
                r < 0
                or r >= ROW
                or c < 0
                or c >= COL
                or board[r][c] != word[i]
                or (r, c) in visit
            ):
                return False
            if len(visit) + 1 == len(word):
                return True

            visit.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if backtrack(r + dr, c + dc, i + 1):
                    return True
            visit.remove((r, c))
            return False

        for r in range(ROW):
            for c in range(COL):
                if backtrack(r, c, 0):
                    return True
        return False
