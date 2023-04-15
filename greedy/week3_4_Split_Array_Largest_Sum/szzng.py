class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)

        while low < high:
            mid = (low+high)//2

            total = 0
            cnt = 1

            for n in nums:
                if total + n <= mid:
                    total += n
                else:
                    total = n
                    cnt += 1

            if cnt > k: low = mid+1
            else: high = mid

        return high
