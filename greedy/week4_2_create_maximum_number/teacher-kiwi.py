class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        res = []
        for i in range(k + 1):
            if i > len(nums1) or k - i > len(nums2):
                continue

            max_nums1 = self.k_max_nums(nums1, i)
            max_nums2 = self.k_max_nums(nums2, k - i)

            max_nums = []
            i, j = 0, 0
            while len(max_nums) < k:
                if max_nums1[i:] > max_nums2[j:]:
                    max_nums.append(max_nums1[i])
                    i += 1
                else:
                    max_nums.append(max_nums2[j])
                    j += 1

            res = max(res, max_nums)
        return res

    def k_max_nums(self, nums, k):
        if k == 0:
            return []

        n = len(nums)
        res = []
        for i in range(n):
            if len(res) + (n - i) == k:
                return res + nums[i:]

            if not res:
                res.append(nums[i])
            elif res[-1] < nums[i]:
                while res and res[-1] < nums[i] and len(res) + (n - i) > k:
                    res.pop()
                res.append(nums[i])
            elif len(res) < k:
                res.append(nums[i])
        return res


# Runtime 535 ms Beats 15.76% // Memory 14.2 MB Beats 79.28%
# 시간 복잡도 O(k^2 * n), 공간 복잡도 O(k)
