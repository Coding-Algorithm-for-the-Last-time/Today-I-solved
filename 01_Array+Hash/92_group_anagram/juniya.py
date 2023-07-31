from collections import Counter

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         hs = {}
#         for i in strs:
#             hs[i] = Counter(i)
#         result = []
#         checked = set()
#         for k1, v1 in hs.items():
#             if k1 in checked:
#                 continue
#             group = [k1]
#             for k2, v2 in hs.items():
#                 if k1 != k2 and v1 == v2:
#                     group.append(k2)
#                     checked.add(k2)
#             result.append(group)
#         return result


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

hs = {}
for i in strs:
    hs[i] = Counter(i)
result = []
checked = set()
for k1, v1 in hs.items():
    if k1 in checked:
        continue
    group = [k1]
    for k2, v2 in hs.items():
        if k1 != k2 and v1 == v2:
            group.append(k2)
            checked.add(k2)
    result.append(group)

print(result)
