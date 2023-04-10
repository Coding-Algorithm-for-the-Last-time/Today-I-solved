# Runtime 555 ms Beats 90.72%
# Memory 31.8 MB Beats 73.9%

from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = {}
        for i in arr:
            cnt[i] = cnt[i] + 1 if i in cnt else 1

        frequency = sorted(list(cnt.values()), reverse=True)
        half_len = len(arr) // 2
        current_len = len(arr)

        for i, f in enumerate(frequency):
            current_len -= f
            if current_len <= half_len: return i + 1
