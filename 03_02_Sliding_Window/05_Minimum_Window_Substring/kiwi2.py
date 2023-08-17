import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t, window = {}, {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        matches = 0
        min_subs = ""
        queue = collections.deque([])
        for i in range(len(s)):
            if s[i] in count_t:
                queue.append(i)
                window[s[i]] = window.get(s[i], 0) + 1
                if window[s[i]] == count_t[s[i]]:
                    matches += 1

            while matches == len(count_t):  # is match
                new_subs = s[queue[0] : queue[-1] + 1]
                min_subs = (
                    min_subs if min_subs and len(min_subs) < len(new_subs) else new_subs
                )

                i = queue.popleft()
                if window[s[i]] == count_t[s[i]]:
                    matches -= 1
                window[s[i]] -= 1

        return min_subs
