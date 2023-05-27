import math
from collections import defaultdict
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = defaultdict(int)
        for num in answers:
            count[num] += 1

        rabbits = 0
        for c in count:
            rabbits += math.ceil(count[c] / (c + 1)) * (c + 1)
        return rabbits

# Runtime 44 ms Beats 65.53% Memory 13.8 MB Beats 92.5%