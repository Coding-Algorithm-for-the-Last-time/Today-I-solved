class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        res = 0
     
        sort_cost = sorted(cost, reverse=True)

        for i in range(len(sort_cost)):
            if (i+1) % 3 != 0:
                res += sort_cost[i]
        
        return res
    

#Runtime 49 ms Beats 47.81%,  Memory 13.8 MB Beats 92.69%

