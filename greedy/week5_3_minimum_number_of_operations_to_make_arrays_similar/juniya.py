import math
# nums와 target을 정렬한 다음 결국 가장 먼곳이 맞춰져야함.

nums = [1,2,5]
target = [4,1,3]

# if nums == target:
#     return 0

nums.sort()
target.sort()

min_diff =abs(math.ceil((nums[0] - target[0]) /2))

max_diff =abs(math.ceil((nums[-1] - target[-1])/2))

print(max(min_diff, max_diff))