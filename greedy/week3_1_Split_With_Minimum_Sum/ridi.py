class Solution:
    def splitNum(self, num: int) -> int:
        l = []
        res = 0
        while num > 0:
            l.append(num % 10)
            num = num // 10
        
        l.sort()
        place = len(l) // 2
        if len(l) % 2 == 0:
            for i in range(0, len(l), 2):
                res += (10 ** (place - 1)) * (l[i] + l[i+1])
                place -= 1
        else:
            pop = l.pop(0)
            res += (10 ** place) * pop
            for i in range(0, len(l), 2):
                res += (10 ** (place - 1)) * (l[i] + l[i+1])
                place -= 1

        return res

    ## so so. Runtime Beats 88.79% / Memory Beats 46.97%
    #TODO 리팩터링!