class Solution:
    def maximum69Number (self, num: int) -> int:
        l = []
        flag = True

        for i in str(num):
            #TODO flag is True or flag == True 필요 없음!!!
            if i == '6' and flag:
                i = '9'
                flag = False
            l.append(i)
        
        return int(''.join(l))
    
    # so so. Runtime Beats 87.77% / Memory Beats 92.51%

    def maximum69Number_two (self, num: int) -> int:
        l = ""
        flag = True

        for i in str(num):
            if i == '6' and flag:
                i = '9'
                flag = False
            l += i
        
        return int(i)

    # Trade off. Runtime Beats 97.20% / Memory Beats 41.52%

    def maximum69Number_three (self, num: int) -> int:
        import re
        #TODO sub(바꾸고 싶은 표현(now), 바꿀 표현(change), 문자열, 횟수)
        return int(re.sub('6','9',str(num),1))