from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def dfs(node, depth=0):
            left_d = depth
            right_d = depth
            if node.left:
                left_d = dfs(node.left, depth + 1)
            if node.right:
                right_d = dfs(node.right, depth + 1)
            diameter[0] = max(diameter[0], left_d + right_d - depth * 2)

            return max(left_d, right_d)

        dfs(root)
        return diameter[0]
