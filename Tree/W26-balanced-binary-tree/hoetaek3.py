from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node, depth=0):
            left_d = depth
            right_d = depth

            res, left_r, right_r = True, True, True
            if node.left:
                left_d, left_r = dfs(node.left, depth + 1)
            if node.right:
                right_d, right_r = dfs(node.right, depth + 1)
            if abs(left_d - right_d) > 1:
                res = False

            return max(left_d, right_d), res and left_r and right_r

        _, answer = dfs(root)

        return answer
