# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head

        _next = head.next
        new_list = ListNode(head.val, None)
        while _next:
            new_list = ListNode(_next.val, new_list)
            _next = _next.next
        return new_list
