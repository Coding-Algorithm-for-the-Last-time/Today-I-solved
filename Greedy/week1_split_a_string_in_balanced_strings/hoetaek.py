from collections import defaultdict

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = defaultdict(int)

        substring_num = 0
        for c in s:
            count[c] += 1

            if count['L'] and count['R'] and count['L'] == count['R']:
                substring_num += 1
                count.clear()

        return substring_num