from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        hs1 = sorted(counter.items(), key=lambda x:x[1], reverse=True)
        result = [x[0] for x in hs1[:k]]
        return result