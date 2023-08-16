from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = defaultdict(int)
        for s in s1:
            dic[s] += 1
        dic2 = defaultdict(int)
        for s in s2[0 : len(s1)]:
            dic2[s] += 1

        print(dic, dic2)
        for i in range(len(s2) - len(s1)):
            if dic == dic2:
                return True
            dic2[s2[i]] -= 1
            if dic2[s2[i]] == 0:
                dic2.pop(s2[i])
            dic2[s2[i + len(s1)]] += 1

        if dic == dic2:
            return True
        return False
