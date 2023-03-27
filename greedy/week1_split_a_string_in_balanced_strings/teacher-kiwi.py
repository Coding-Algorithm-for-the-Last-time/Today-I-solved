class Solution:
    def balancedStringSplit(self, s: str) -> int:
        check, res = 0, 0
        # s를 하나씩 보면서
        # "R"이면 check를 +1
        # "L"이면 check를 -1
        # check가 0일 때 하나씩 센 후 센 값을 리턴
        for char in s:
            check += 1 if char == "R" else -1
            if check == 0:
                res += 1
        return res
