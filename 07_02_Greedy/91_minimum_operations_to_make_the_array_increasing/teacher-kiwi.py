class Solution:
    def minOperations(self, nums: list[int]) -> int:
        # 1. 숫자를 하나씩 보면서 이전 숫자를 기억한다.
        # 2. 새로운 숫자와 이전 숫자를 비교해서 새로운 숫자가 더 크면 continue!
        # 3. 이전 숫자가 더 크면 새로운 숫자를 이전 숫자보다 1 크게 만들고 횟수를 누적한다.
        pre_num, res = 0, 0
        for num in nums:
            if pre_num < num:
                pre_num = num
            else:
                res += pre_num - num + 1
                pre_num += 1
        return res
