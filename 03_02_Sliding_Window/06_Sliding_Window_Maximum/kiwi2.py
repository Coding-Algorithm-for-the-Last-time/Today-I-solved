import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_list = []
        mono_queue = collections.deque()
        l, r = 0, 0

        while r < len(nums):
            while mono_queue and nums[mono_queue[-1]] < nums[r]:
                mono_queue.pop()
            mono_queue.append(r)

            if l > mono_queue[0]:
                mono_queue.popleft()

            if r >= k - 1:
                max_list.append(nums[mono_queue[0]])
                l += 1
            r += 1

        return max_list
