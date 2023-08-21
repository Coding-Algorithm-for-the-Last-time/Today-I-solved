# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp, slow.next = slow.next, None

        pre, post = head, None
        while temp:
            post = ListNode(temp.val, post)
            temp = temp.next
        while post:
            temp = post.next
            pre.next, post.next = post, pre.next
            pre, post = pre.next.next, temp
