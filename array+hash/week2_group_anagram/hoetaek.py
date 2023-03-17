from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram = defaultdict(list)
        for string in strs:
            trans_string = "".join(sorted(string))
            group_anagram[trans_string].append(string)
        return list(group_anagram.values())
