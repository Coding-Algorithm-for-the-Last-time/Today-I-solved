from collections import Counter
import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
       
        cnt = Counter(answers)

        res = 0

        for k,v in cnt.items():
            if k >= v:
                res += k+1

            else:
                res += math.ceil(v/(k+1))*(k+1)

        return (res)