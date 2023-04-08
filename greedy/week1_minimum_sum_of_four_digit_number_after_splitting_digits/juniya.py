class Solution:
    def minimumSum(self, num: int) -> int:
        nums = list(str(num))
        nums = sorted(nums)
        return int(nums[0]+nums[3]) +int(nums[1]+nums[2])

#4자리숫자를 작은순서대로 솔트하고난 다음에 합산이 가장 작은 조합인 인덱서 0과 3으로 수를 하나 만들고 1과 2로 숫자하나 만들어서 더하기
