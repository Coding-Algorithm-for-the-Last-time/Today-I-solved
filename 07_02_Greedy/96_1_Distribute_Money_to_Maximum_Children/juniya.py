
#조건1. 아이들에게 모든 money를 나눠줘야함
#조건2. 4달러 받은 아이는 없어야함.
#조건3. 모든 아이들은 최소 1달러를 받야아함.


class Solution:
    def distMoney(self, money: int, children: int) -> int:
      
      if money < children:
         return -1
      
      money = money - children
      
      if money > children *7:
          return children -1
      elif money // 7 == children -1 and money % 7 == 3:
          return money //7 -1
      else:
          return money //7