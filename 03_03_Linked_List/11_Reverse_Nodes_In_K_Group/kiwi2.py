# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        dummy = prev_tail = ListNode(0, head)

        while True:
            target = prev_tail
            for _ in range(k):
                if not target.next:
                    return dummy.next
                target = target.next

            point = curr_tail = prev_tail.next
            while point != target:
                temp = point.next
                point.next = target.next
                target.next = point
                point = temp
            prev_tail.next = target
            prev_tail = curr_tail
