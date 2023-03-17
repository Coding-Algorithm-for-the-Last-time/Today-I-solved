from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = defaultdict(int)
        for num in nums:
            hs[num] += 1
        return [i[0] for i in sorted(hs.items(), key=lambda x: x[1], reverse=True)[:k]]
