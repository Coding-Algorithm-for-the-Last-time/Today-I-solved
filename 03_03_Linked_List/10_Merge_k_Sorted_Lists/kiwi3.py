from heapq import heappush, heappop


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
        head = point = ListNode()
        while heap:
            index = heappop(heap)[1]
            point.next = lists[index]
            if point.next.next:
                lists[index] = point.next.next
                heappush(heap, (point.next.next.val, index))
            point = point.next
        return head.next
