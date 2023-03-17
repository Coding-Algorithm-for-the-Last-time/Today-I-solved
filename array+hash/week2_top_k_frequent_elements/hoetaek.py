from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs = defaultdict(int)
        for num in nums:
            hs[num] += 1
        return [i[0] for i in sorted(hs.items(), key=lambda x: x[1], reverse=True)[:k]]

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = Counter(nums)
        return [i[0] for i in n.most_common(k)]
    
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)

        answer = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                answer.append(j)
                if len(answer) == k:
                    return answer