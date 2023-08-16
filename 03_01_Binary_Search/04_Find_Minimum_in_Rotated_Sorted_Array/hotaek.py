class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count, s2_count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1_count[i] == s2_count[i] else 0

        for i in range(len(s2) - len(s1)):
            if matches == 26:
                return True

            l = ord(s2[i]) - ord("a")
            s2_count[l] -= 1
            if s2_count[l] == s1_count[l]:
                matches += 1
            elif s1_count[l] - 1 == s2_count[l]:
                matches -= 1

            r = ord(s2[i + len(s1)]) - ord("a")
            s2_count[r] += 1
            if s2_count[r] == s1_count[r]:
                matches += 1
            elif s1_count[r] + 1 == s2_count[r]:
                matches -= 1

        return matches == 26
