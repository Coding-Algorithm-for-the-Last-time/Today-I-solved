class Solution:
    def characterReplacement(self, string: str, k: int) -> int:
        count = {}
        max_sub_length = 0
        L = 0
        for R in range(len(string)):
            count[string[R]] = count.get(string[R], 0) + 1
            if R - L + 1 - max(count.values()) <= k:
                max_sub_length = max(max_sub_length, R - L + 1)
            while R - L + 1 - max(count.values()) > k and L < R:
                count[string[L]] -= 1
                L += 1
        return max_sub_length