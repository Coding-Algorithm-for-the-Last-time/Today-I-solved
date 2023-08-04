from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([(root, 0)])

        res = []

        level = 0

        while q:
            head, level = q.popleft()
            if not head:
                break

            if q and level != q[0][1]:
                res.append(head.val)
            elif not q:
                res.append(head.val)

            if head.left:
                q.append((head.left, level + 1))
            if head.right:
                q.append((head.right, level + 1))
        return res
