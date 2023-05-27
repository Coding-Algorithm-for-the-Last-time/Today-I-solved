class Solution:
    def maximumTop(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            if k % 2 == 1:
                return -1
            else:
                return nums[0]

        if k < 2:
            return nums[k]

        max_num_index = 0
        for i in range(len(nums[:k])):
            if nums[i] > nums[max_num_index]:
                max_num_index = i

        if max_num_index + 1 == k:
            if len(nums) > k:
                return max(max(nums[0 : k - 1]), nums[k])
            return max(nums[0 : k - 1])
        return max(nums[0 : k + 1])
