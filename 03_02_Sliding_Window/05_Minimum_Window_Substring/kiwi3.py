class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t, window = {}, {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        matches = 0
        min_subs = ""
        l = 0
        for r in range(len(s)):
            if s[r] in count_t:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == count_t[s[r]]:
                    matches += 1

            while matches == len(count_t):  # is match
                if s[l] in count_t:
                    if window[s[l]] == count_t[s[l]]:
                        matches -= 1
                    window[s[l]] -= 1

                    new_subs = s[l : r + 1]
                    min_subs = (
                        min_subs
                        if min_subs and len(min_subs) < len(new_subs)
                        else new_subs
                    )
                l += 1

        return min_subs
