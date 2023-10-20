class Solution:
    def longestPalindrome(self, s: str) -> str:
        # odd
        centers = range(len(s))
        i = 1
        while i <= len(s) // 2:
            temp = []
            for center in centers:
                if (
                    center - i >= 0
                    and center + i < len(s)
                    and s[center - i] == s[center + i]
                ):
                    temp.append(center)
            if not temp:
                break
            i += 1
            centers = temp
        palindrome1 = s[centers[0] - i + 1 : centers[0] + i]

        # even
        centers = range(len(s))
        i = 0
        while i <= len(s) // 2:
            temp = []
            for center in centers:
                if (
                    center - i >= 0
                    and center + i + 1 < len(s)
                    and s[center - i] == s[center + i + 1]
                ):
                    temp.append(center)
            if not temp:
                break
            i += 1
            centers = temp
        palindrome2 = s[centers[0] - i + 1 : centers[0] + i + 1]
        return palindrome1 if len(palindrome1) >= len(palindrome2) else palindrome2
