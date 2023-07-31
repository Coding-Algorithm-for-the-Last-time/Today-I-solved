from typing import List

# 가장 많이 할인을 받아야 한다 -> 내림 차순 정렬
def minimumCost(self, cost: List[int]) -> int:
    cost.sort(reverse=True)
    res = 0

    # for loop 도는게 시간 복잡도 이득 없음
    # 오히려 공간 복잡도 손해(필요 없는 변수 선언)

    loop = len(cost) // 3
    remain = len(cost) % 3
    for i in range(loop):
        res += (cost[3 * i] + cost[3 * i + 1])
    for i in range(remain):
        res += cost[(-1) - i]
    
    return res

    # so so. Runtime Beats 58.79% / Memory Beats 92.53%