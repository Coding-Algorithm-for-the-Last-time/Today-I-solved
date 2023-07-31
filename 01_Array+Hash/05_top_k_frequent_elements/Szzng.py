from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_num = {}
        for i in nums:
            count_num[i] = count_num[i] + 1 if i in count_num else 1

        max_values = sorted(list(count_num.values()), reverse=True)[:k]

        return [key for key, value in count_num.items() if value in max_values]
