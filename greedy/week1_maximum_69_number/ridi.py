class Solution:
    def maximum69Number (self, num: int) -> int:
        l = []
        flag = True

        for i in str(num):
            if i == '6' and flag is True:
                i = '9'
                flag = False
            l.append(i)
        
        return int(''.join(l))