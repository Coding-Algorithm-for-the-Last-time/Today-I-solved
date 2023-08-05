# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        h, t = None, head

        while t:
            temp, t.next = t.next, h
            h, t = t, temp

        return h
