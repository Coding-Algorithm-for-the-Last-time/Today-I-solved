# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        res = ListNode(0)
        temp = res
        plus_one = 0
        while l1 or l2:
            digit10, digit1 = divmod(
                (l1 and l1.val or 0) + (l2 and l2.val or 0) + plus_one, 10
            )
            temp.next = ListNode(digit1)
            plus_one = digit10
            l1, l2, temp = l1 and l1.next or 0, l2 and l2.next or 0, temp.next
        if plus_one:
            temp.next = ListNode(1)
        return res.next
