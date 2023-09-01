# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node | None) -> Node | None:
        copied_list = {None: None}
        res = Node(0)
        temp = res
        while head:
            if head.next not in copied_list:
                copied_list[head.next] = Node(0)
            if head.random not in copied_list:
                copied_list[head.random] = Node(0)
            if head in copied_list:
                copied_list[head].val = head.val
                copied_list[head].next = copied_list[head.next]
                copied_list[head].random = copied_list[head.random]
            else:
                copied_list[head] = Node(
                    head.val, copied_list[head.next], copied_list[head.random]
                )
            temp.next = copied_list[head]
            temp, head = temp.next, head.next
        return res.next
