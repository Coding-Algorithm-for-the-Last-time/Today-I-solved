class Solution:
    def calc_happy(self, n: int) -> int:
        num = 0
        while n:
            num += (n % 10) ** 2
            n //= 10
        return num

    def isHappy(self, n: int) -> bool:
        nums = set()
        while n != 1:
            if n in nums:
                return False
            nums.add(n)
            n = self.calc_happy(n)
        return True
