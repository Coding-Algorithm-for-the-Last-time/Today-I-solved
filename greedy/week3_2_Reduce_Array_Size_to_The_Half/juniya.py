from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        res = 0
        freq = Counter(arr)
        sorted_freq = sorted(freq.values(), reverse=True) 
        sum = 0

        for v in sorted_freq:
            sum += v
            res += 1
            if sum >= (len(arr)//2):
                break

        return (res)



