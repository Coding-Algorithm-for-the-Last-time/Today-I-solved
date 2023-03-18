class Solution:
    def topKFrequent(self, nums, k):
        counter = {}
        for num in nums:
            if num in counter: 
                counter[num][1] += 1
            else: 
                counter[num] = [num, 1]
        return [i[0] for i in sorted(counter.values(), key=lambda x:x[1], reverse=True)[:k]]