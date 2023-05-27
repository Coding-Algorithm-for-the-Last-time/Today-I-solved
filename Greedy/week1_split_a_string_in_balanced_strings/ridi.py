class Solution:
    def balancedStringSplit(self, s: str) -> int:
        d = {'R':0, 'L':0}
        res = 0

        for c in s:
            d[c] = d[c] + 1
            if d['R'] == d['L']:
                res += 1
                d = {'R':0, 'L':0}

        return res

    ## very bad. Runtime Beats 18.7% / Memory Beats 46.46%

    def balancedStringSplit_two(self, s: str) -> int:
        flag = 0
        res = 0
        for c in s:
            if c == "R":
                flag += 1
            else:
                flag -= 1
            if flag == 0:
                res += 1
        
        return res
    
    ## so so. Runtime Beats 71.95% / Memory Beats 94.11%