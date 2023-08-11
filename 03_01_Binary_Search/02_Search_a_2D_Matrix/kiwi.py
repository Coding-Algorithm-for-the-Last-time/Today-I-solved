class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        down, up = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        c_h, c_w = 0, 0

        while down <= up:
            c_h = down + (up - down) // 2
            if matrix[c_h][left] > target:
                up = c_h - 1
            elif matrix[c_h][right] < target:
                down = c_h + 1
            else:
                break

        while left <= right:
            c_w = left + (right - left) // 2
            if matrix[c_h][c_w] < target:
                left = c_w + 1
            elif matrix[c_h][c_w] > target:
                right = c_w - 1
            else:
                return True
        return False
