# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         hs = {}
#         for i in nums:
#             hs[i] = nums.count(i)
#         hs1 = sorted(hs.items(), key=lambda x:x[1], reverse=True)
#         result = []
#         for i in range(k):
#             result += [(hs1[i][0])]
#         return result



nums = [1,1,1,2,2,3]
k = 2

hs = {}
for i in nums:
    hs[i] = nums.count(i)
hs1 = sorted(hs.items(), key=lambda x:x[1], reverse=True)
result = []
for i in range(k):
    result += [(hs1[i][0])]
# return result


print(result)