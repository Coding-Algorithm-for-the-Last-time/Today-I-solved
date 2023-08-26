# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head.next:
            return None

        slow, fast = head, head.next.next
        size = 2
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            size += 2

        target = size - n + 1 if fast else size - n
        if target == 0:
            return head.next
        temp = head
        for i in range(target - 1):
            temp = temp.next
        temp.next = temp.next.next
        return head
