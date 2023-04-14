from collections import Counter

class Solution:
    def splitNum(self, num: int) -> int:
        freq = Counter(str(num))

        num1 =""
        num2 =""

        keys = sorted(freq.keys())

        while sum(freq.values()) > 0:
            for i in keys:
                if freq[i] >0:
                    num1 += i
                    freq[i] -= 1
                    break

            for i in keys:
                if freq[i] >0:
                    num2 += i
                    freq[i] -= 1
                    break

        return int(num1) + int(num2)