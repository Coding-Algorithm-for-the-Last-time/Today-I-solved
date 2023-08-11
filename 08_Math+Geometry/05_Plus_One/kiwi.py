class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        flag = True
        i = len(digits)
        while flag and i:
            i -= 1
            if digits[i] == 9:
                digits[i] = 0
                flag = True
            else:
                digits[i] += 1
                flag = False
        return [1] + digits if flag else digits
