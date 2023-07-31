from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqs = defaultdict(set)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in rows[i] or val in cols[j] or val in sqs[(i // 3, j // 3)]:
                    return False
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    sqs[(i // 3, j // 3)].add(val)
        return True
