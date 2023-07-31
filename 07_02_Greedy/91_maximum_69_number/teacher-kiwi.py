class Solution:
    def maximum69Number(self, num: int) -> int:
        # 1. num을 문자열로 바꾼다.
        # 2. 첫번째로 나오는 "6"을 "9"로 바꾼다.
        # 3. 정수형으로 바꾼 뒤 리턴!
        return int(str(num).replace("6", "9", 1))


####################################################


class Solution:
    def maximum69Number(self, num: int) -> int:
        digit = 0
        # 1. num의 자리수를 센다.
        while num // 10**digit > 0:
            digit += 1
        while digit > 0:
            # 2. 맨 앞 자리 부터 차례대로 6인지 확인한다.
            if num // 10 ** (digit - 1) % 10 == 6:
                # 3. 6이 나오면 해당 자리에 3을 더하고 리턴!
                return num + 3 * 10 ** (digit - 1)
            digit -= 1
        return num
