import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, (-stone, stone))
        while len(heap) > 1:
            _, x = heapq.heappop(heap)
            _, y = heapq.heappop(heap)
            if x - y > 0:
                heapq.heappush(heap, (y - x, x - y))
        return heap[0][1] if heap else 0
