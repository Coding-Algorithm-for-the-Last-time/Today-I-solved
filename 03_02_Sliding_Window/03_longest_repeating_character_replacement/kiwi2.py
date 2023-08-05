class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        left = 0
        maxf = 0
        for right in range(len(s)):
            cnt[s[right]] = 1 + cnt.get(s[right], 0)
            maxf = max(maxf, cnt[s[right]])
            if (right - left + 1) - maxf > k:
                cnt[s[left]] -= 1
                left += 1
        return right - left + 1
