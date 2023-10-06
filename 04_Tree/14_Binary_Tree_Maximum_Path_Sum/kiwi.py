# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        res = [float("-inf")]

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res[0] = max(
                res[0],
                node.val,
                node.val + left,
                node.val + right,
                node.val + left + right,
            )
            node.val += max(0, left, right)
            return node.val

        dfs(root)
        return res[0]
