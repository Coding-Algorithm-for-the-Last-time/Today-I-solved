# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None
        dummy = ListNode(float("-inf"))
        temp = dummy
        for li in lists:
            while temp.next:
                if not li:
                    break
                if temp.next.val > li.val:
                    nxt = temp.next
                    temp.next = li
                    li = li.next
                    temp.next.next = nxt
                temp = temp.next
            if li:
                temp.next = li
            temp = dummy
        return dummy.next
