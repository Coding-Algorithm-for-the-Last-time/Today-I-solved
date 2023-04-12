class Solution:
    def splitNum(self, num: int) -> int:
        l = []
        res = 0
        while num > 0:
            l.append(num % 10)
            num = num // 10
        
        l.sort()
        place = len(l) // 2
        if len(l) % 2 != 0:
            pop = l.pop(0)
            res += (10 ** place) * pop        
        for i in range(0, len(l), 2):
            res += (10 ** (place - 1)) * (l[i] + l[i+1])
            place -= 1

        return res

    # Runtime 27ms Beats 88.79%
    # Memory 13.8MB Beats 94.15%

    #TODO 리팩터링!