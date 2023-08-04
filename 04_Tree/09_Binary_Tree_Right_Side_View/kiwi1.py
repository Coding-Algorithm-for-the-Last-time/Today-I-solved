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
        if not root:
            return res

        queue = deque([(root, 0)])
        current_floor = 0
        temp = root.val
        while queue:
            node, floor = queue.popleft()
            if current_floor != floor:
                res.append(temp)
                current_floor += 1
            if node.left:
                queue.append((node.left, floor + 1))
            if node.right:
                queue.append((node.right, floor + 1))
            temp = node.val

        return res + [temp]
