class Solution:
    def minimumSum(self, num: int) -> int:
        num_str = str(num)
        num_li = sorted(num_str)
        return int(num_li[0] + num_li[2]) + int(num_li[1] + num_li[3])