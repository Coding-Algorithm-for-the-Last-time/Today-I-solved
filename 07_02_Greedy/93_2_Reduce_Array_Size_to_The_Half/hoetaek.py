from collections import defaultdict
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = defaultdict(int)
        for i in arr:
            count[i] += 1

        arr_len = len(arr)
        remove_num = 0
        for i, count_num in enumerate(sorted(count.values(), reverse=True)):
            remove_num += count_num
            if remove_num >= arr_len // 2:
                return i + 1


# Runtime 597 ms Beats 59.58% Memory 31.3 MB Beats 90.7%
