# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        node_list = []
        temp = head
        while temp:
            node_list.append(temp)
            temp = temp.next
        length = len(node_list)
        node_list.append(None)
        res = temp = ListNode()
        for i in range(length // k):
            for j in range(k):
                temp.next = node_list[i * k + k - j - 1]
                temp = temp.next
        temp.next = node_list[i * k + k]
        return res.next
