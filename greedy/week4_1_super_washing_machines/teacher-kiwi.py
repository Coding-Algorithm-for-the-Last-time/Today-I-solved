class Solution:
    def findMinMoves(self, machines: list[int]) -> int:
        s = sum(machines)
        n = len(machines)
        if s % n:
            return -1

        target = s // n
        count = 0
        move = 0
        for i in range(n):
            delta = machines[i] - target
            move += delta
            count = max(count, abs(move), delta)

        return count


# Runtime 92 ms Beats 19.69% // Memory 14.9 MB Beats 32.12%
# 시간 복잡도 O(n), 공간 복잡도 O(1)
