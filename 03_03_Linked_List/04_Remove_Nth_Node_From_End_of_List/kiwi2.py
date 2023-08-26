# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        res = ListNode(0, head)
        target = res
        end = head

        for _ in range(n):
            end = end.next

        while end:
            target = target.next
            end = end.next

        target.next = target.next.next
        return res.next
