class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = "".join([w.lower() for w in s if w.isalnum()])
        return alnum == alnum[::-1]
