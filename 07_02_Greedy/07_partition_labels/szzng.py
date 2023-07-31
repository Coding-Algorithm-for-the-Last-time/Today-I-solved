# Runtime 34 ms Beats 92.54%
# Memory 13.9 MB Beats 55.57%

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {s[i]: i for i in range(len(s))}
        result = []
        size, end = 0, 0

        for i, v in enumerate(s):
            size += 1
            end = max(end, last_index[v])
            if i == end:
                result.append(size)
                size = 0

        return result
