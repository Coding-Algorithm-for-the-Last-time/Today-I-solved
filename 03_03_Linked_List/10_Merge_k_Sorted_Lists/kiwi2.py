# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        li1 = lists.pop()
        while lists:
            node = temp = ListNode()
            li2 = lists.pop()
            while li1 and li2:
                if li1.val < li2.val:
                    temp.next = li1
                    li1 = li1.next
                else:
                    temp.next = li2
                    li2 = li2.next
                temp = temp.next
            temp.next = li1 or li2
            li1 = node.next
        return li1
