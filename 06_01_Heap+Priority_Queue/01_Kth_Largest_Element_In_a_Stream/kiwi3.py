import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.nums = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
