class Solution:
    def calc_happy(self, n: int) -> int:
        num = 0
        while n:
            num += (n % 10) ** 2
            n //= 10
        return num

    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.calc_happy(n)
        while slow != fast:
            fast = self.calc_happy(self.calc_happy(fast))
            slow = self.calc_happy(slow)
        return True if fast == 1 else False
