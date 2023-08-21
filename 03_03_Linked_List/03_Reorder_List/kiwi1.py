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

        pre = head
        post = slow.next
        slow.next = None

        temp = None
        while post:
            temp = ListNode(post.val, temp)
            post = post.next
        post = temp

        while pre and post:
            temp = post.next
            pre.next, post.next = post, pre.next
            pre, post = pre.next.next, temp
