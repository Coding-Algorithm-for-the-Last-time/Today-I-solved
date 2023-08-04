from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        res = []
        queue = deque([root])
        while queue:
            right_side = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    right_side = node.val
                    queue.append(node.left)
                    queue.append(node.right)
            if right_side is not None:
                res.append(right_side)
        return res
