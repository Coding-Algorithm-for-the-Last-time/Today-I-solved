class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in s:
            if 65 <= ord(i) <= 90:
                new_s += chr(ord(i) + 32)
            elif 97 <= ord(i) <= 122:
                new_s += i
            elif 48 <= ord(i) <= 57:
                new_s += i
            else:
                pass
        if not new_s:
            return True

        l = 0
        r = len(new_s) - 1
        while l < r:
            if new_s[l] == new_s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
