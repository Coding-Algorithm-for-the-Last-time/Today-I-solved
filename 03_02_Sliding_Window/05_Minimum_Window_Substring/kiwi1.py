import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_words = [0] * 58
        sub_words = [0] * 58
        for w in t:
            t_words[ord(w) - ord("A")] += 1

        matches = 0
        for i in range(len(t_words)):
            if t_words[i] == sub_words[i]:
                matches += 1

        min_subs = ""
        queue = collections.deque([])
        for i in range(len(s)):
            w_id = ord(s[i]) - ord("A")
            if t_words[w_id] > 0:
                sub_words[w_id] += 1
                if sub_words[w_id] == t_words[w_id]:
                    matches += 1
                queue.append(i)
            while matches == 58:  # is match
                new_subs = s[queue[0] : queue[-1] + 1]
                min_subs = (
                    min_subs if min_subs and len(min_subs) < len(new_subs) else new_subs
                )

                w_id = ord(s[queue.popleft()]) - ord("A")
                if sub_words[w_id] == t_words[w_id]:
                    matches -= 1
                sub_words[w_id] -= 1

        return min_subs
