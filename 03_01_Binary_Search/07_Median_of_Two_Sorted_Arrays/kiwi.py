from math import inf


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        sum_len = len(nums1) + len(nums2)
        center = sum_len // 2 - 1

        l, r = 0, len(nums1) - 1
        while True:
            c_nums1 = l + (r - l) // 2
            c_nums2 = center - c_nums1

            l_nums1 = nums1[c_nums1] if c_nums1 >= 0 else -inf
            r_nums1 = nums1[c_nums1 + 1] if c_nums1 + 1 <= len(nums1) - 1 else inf
            l_nums2 = nums2[c_nums2 - 1] if c_nums2 - 1 >= 0 else -inf
            r_nums2 = nums2[c_nums2] if c_nums2 <= len(nums2) - 1 else inf

            if l_nums1 <= r_nums2 and l_nums2 <= r_nums1:
                print(l_nums1, r_nums1, l_nums2, r_nums2)
                if sum_len % 2 == 0:
                    return (max(l_nums1, l_nums2) + min(r_nums1, r_nums2)) / 2
                return min(r_nums1, r_nums2)
            elif l_nums1 > r_nums2:
                r = c_nums1 - 1
            else:
                l = c_nums1 + 1
