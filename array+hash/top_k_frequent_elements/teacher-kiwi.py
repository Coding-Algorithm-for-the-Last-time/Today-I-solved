class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for num in nums:
            if num in num_dict: num_dict[num][1] += 1
            else: num_dict[num] = [num, 1]
        return [li[0] for li in sorted(num_dict.values(), key=lambda x: x[1], reverse=True)[:k]]