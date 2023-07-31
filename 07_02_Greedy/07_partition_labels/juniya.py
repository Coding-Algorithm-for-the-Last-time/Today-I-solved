# #방법 1. find와 rfind를 활용해서 인덱스값을 구함. find, rfind를 사용하면 시간복잡도가 O(n^2)이라 시간초과됨

# s = "ababcbacadefegdehijhklij"
# n = len(s)
# res = []
# i = 0

# while i < len(s):
#     first_index = s.find(s[i])
#     last_index = s.rfind(s[i])
#     for j in range(first_index, last_index):
#         if s.rfind(s[j]) <= last_index:
#             continue
#         last_index = s.rfind(s[j])
    
#     res.append(s[first_index:last_index+1])
    
#     i = last_index

# print(res)

#방법2. gpt에게 시간복잡도 해결방안 물어보니, last_indexes로 각 문자열의 마지막 인덱스를 저장하는 딕셔너리를 만드는걸 추천함.
#문자열을 순회하면서 각 문자열의 마지막인덱스값과 기존의 last_index값을 비교하여 큰 값을 last_index로 지정하고 문자열의 인덱스와 last_index가 일치하면 파티션함.
#i를 파티션한 마지막 문자+1로 변경

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        res = []
        last_indexes = {}

        for i in range(n):
            last_indexes[s[i]] = i

        i = 0
        last_index = 0
        for j in range(n):
            last_index = max(last_index, last_indexes[s[j]])
            if j == last_index:
                res.append(j - i + 1)
                i = j + 1

        return res
    
# Runtime 35 ms Beats 90.81% Memory 13.8 MB Beats 55.57%