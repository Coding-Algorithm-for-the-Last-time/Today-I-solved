
# #음수와 0 제거
# nums = [num for num in nums if num > 0 ]

# #작은수부터 정렬
# nums = sorted(nums)

# #1부터 비교 nums에 없는 가장 작은 자연수 출력
# i = 0
# while True:
#     i += 1
#     if i not in nums:
#         print(i)
#         break


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        num_set = set(range(1, n+1))
        for num in nums:
            if num in num_set:
                num_set.remove(num)
        if len(num_set) == 0:
            return n+1
        else:
            return min(num_set)