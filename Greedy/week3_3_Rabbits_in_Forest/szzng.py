from math import ceil
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        result = 0
        cnt = {}
        for i in answers:
            cnt[i] = cnt[i] + 1 if i in cnt else 1

        for k, v in cnt.items():
            result += ceil(v / (k + 1)) * (k + 1)

        return result
