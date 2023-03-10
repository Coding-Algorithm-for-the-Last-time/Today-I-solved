from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hs = set()
        for i in nums:
            if i not in hs:
                hs.add(i)
            else:
                return True
        return False
