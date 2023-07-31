class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0 
        if len(nums) < 2:
            return 0

        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                count += nums[i] + 1 -nums[i+1]
                nums[i+1] = nums[i]+1
        return count
    

#if문은 만약 주어진 리스트안에 변수가 2개보다 작으면 작업을 할 필요가 없어서 0을 리터
#2개 이상일경우에는 for문을 돌려서 nums[i]가 num[i+1]보다 크거나 같으면 nums[i+1]을 nums[i]보다 1 더 크게 만들고 그 차이를 count에 저장
