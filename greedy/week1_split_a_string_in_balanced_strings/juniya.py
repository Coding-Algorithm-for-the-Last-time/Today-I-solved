class Solution:
    def balancedStringSplit(self, s: str) -> int:
        left, right = 0, 0
        check_LR = {"R": 0, "L": 0}
        count = 0 

        while right < len(s):
            if s[right] == next(iter(check_LR)):
                check_LR["R"] += 1

            else:
                check_LR["L"] += 1

            if check_LR["R"] == check_LR["L"]:
                count +=1
                left = right

            right +=1

        return count 
