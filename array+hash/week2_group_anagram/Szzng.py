from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}

        for i in strs:
            sorted_str = ''.join(sorted(i))
            if sorted_str in count:
                count[sorted_str].append(i)
            else:
                count[sorted_str] = [i]

        return list(count.values())
