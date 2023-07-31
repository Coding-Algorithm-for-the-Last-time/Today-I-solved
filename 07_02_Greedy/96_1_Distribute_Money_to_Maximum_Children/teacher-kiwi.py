class Solution:
    def distMoney(self, money: int, children: int) -> int:
        remaining_money = money - children
        if remaining_money < 0:
            return -1
        elif remaining_money > children * 7:
            return children - 1
        elif remaining_money // 7 == children - 1 and remaining_money % 7 == 3:
            return remaining_money // 7 - 1
        else:
            return remaining_money // 7
