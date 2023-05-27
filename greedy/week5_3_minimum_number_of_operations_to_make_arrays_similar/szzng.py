class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()
        n_even, n_odd, t_even, t_odd = [], [], [], []

        for i in range(len(nums)):
            if nums[i]%2: n_odd.append(nums[i])
            else: n_even.append(nums[i])
            if target[i]%2: t_odd.append(target[i])
            else: t_even.append(target[i])

        res = 0
        for i in range(len(n_odd)):
            if t_odd[i]>n_odd[i]:
                res += t_odd[i]-n_odd[i]
        
        for i in range(len(n_even)):
            if t_even[i]>n_even[i]:
                res += t_even[i]-n_even[i]

        return res//2
