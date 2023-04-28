# 1. 오른차순으로 정렬
# 2. 가장 낮은 수부터 그 다음수랑 같게끔 만들어줌 k값을 사용한 만큼 제외하고 만약 k값이 0이면 break
# 3. for문을 돌렸는데 k값이 남으면 전체 배열에 순서대로 +1씩 해줌 k값이 0이 되면 break
# 4. 전체 배열의 곱을 result에 넘기기 
# 시간복잡도가 커서 시간 초과됨..

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        modulo = 10**9 +7
        result = 1
        nums.sort()
        n = len(nums)

        for i in range(n-1):
            while nums[i] != nums[i+1]:
                nums[i] += 1
                k -= 1
                if k == 0:
                    break

        while k != 0:
            for i in range(n):
                nums[i] += 1
                k -= 1
                if k == 0:
                    break

        for num in nums:
            result = (result * num) % modulo

        return result