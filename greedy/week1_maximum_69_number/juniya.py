class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        for i in range(len(s)):
            if s[i] == "6":
                s[i] = "9"
                break
        
        return(int("".join(s)))
    
#가장 왼쪽부터 훑으면서 처음 나오는 6을 9로 바꿈.
