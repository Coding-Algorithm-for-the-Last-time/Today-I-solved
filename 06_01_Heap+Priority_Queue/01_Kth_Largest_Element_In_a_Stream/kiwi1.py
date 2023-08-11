class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums = sorted(self.nums + [val], reverse=True)
        return self.nums[self.k - 1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
