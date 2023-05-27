class Solution:
    def minimumSum(self, num: int) -> int:
        l = [i for i in str(num)]
        l.sort()
        return int(l[0] + l[3]) + int(l[1] + l[2])
    
    # so so. Runtime Beats 41.97% / Memory Beats 41.73%

    def minimumSum_faster(self, num: int) -> int:
        d = [0] * 10
        for _ in range(4):
            n = num % 10
            d[n] += 1
            num = num // 10

        res = 0
        tens = 2
        for i in range(10):
            k = d[i]
            while k > 0:
                if tens > 0:
                    res += i * 10
                    tens -= 1
                else:
                    res += i
                k -= 1
                
        return res

    # extreme somewhat. Runtime Beats 72.67% / Memory Beats 5.30%