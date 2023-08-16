class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_cnt = [0] * 26
        s2_cnt = [0] * 26
        for i in range(len(s1)):
            s1_cnt[ord(s1[i]) - ord("a")] += 1
            s2_cnt[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if s1_cnt[i] == s2_cnt[i]:
                matches += 1

        for i in range(len(s2) - len(s1)):
            l, r = ord(s2[i]) - ord("a"), ord(s2[i + len(s1)]) - ord("a")

            if matches == 26:
                return True

            s2_cnt[l] -= 1
            if s2_cnt[l] == s1_cnt[l]:
                matches += 1
            elif s2_cnt[l] + 1 == s1_cnt[l]:
                matches -= 1

            s2_cnt[r] += 1
            if s2_cnt[r] == s1_cnt[r]:
                matches += 1
            elif s2_cnt[r] - 1 == s1_cnt[r]:
                matches -= 1

        return matches == 26
