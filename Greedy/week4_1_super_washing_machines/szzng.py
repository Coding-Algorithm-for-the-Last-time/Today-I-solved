class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        if sum(machines)%len(machines): return -1

        average = sum(machines)//len(machines)
        maximum = max(machines) - average
        acc = 0
        for m in machines:
            acc += m-average
            maximum = max(maximum, abs(acc))

        return maximum
