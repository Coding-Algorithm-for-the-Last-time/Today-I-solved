from typing import List


def isValidSudoku(self, board: List[List[str]]) -> bool:
    for i in range(9):
        temp = []
        for j in range(9):
            if board[i][j] != ".":
                if board[i][j] not in temp:
                    temp.append(board[i][j])
                else:
                    return False

    for i in range(9):
        temp = []
        for j in range(9):
            if board[j][i] != ".":
                if board[j][i] not in temp:
                    temp.append(board[j][i])
                else:
                    return False

    for i in range(3):
        for j in range(3):
            print(i * 3, j * 3)
            temp = []
            for k in range(3):
                for l in range(3):
                    if board[i * 3 + k][j * 3 + l] != ".":
                        if board[i * 3 + k][j * 3 + l] not in temp:
                            temp.append(board[i * 3 + k][j * 3 + l])
                        else:
                            return False

    return True
