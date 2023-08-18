import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        max_list = []
        mono_queue = collections.deque()

        for i in range(k):
            while mono_queue and mono_queue[-1] < nums[i]:
                mono_queue.pop()
            mono_queue.append(nums[i])
        max_list.append(mono_queue[0])

        for i in range(k, len(nums)):
            out = nums[i - k]
            if out == mono_queue[0]:
                mono_queue.popleft()
            while mono_queue and mono_queue[-1] < nums[i]:
                mono_queue.pop()
            mono_queue.append(nums[i])
            max_list.append(mono_queue[0])

        return max_list
