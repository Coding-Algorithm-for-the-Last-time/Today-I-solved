from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root, res=[]):
            if not root:
                res.append(None)
                return
            res.append(root.val)
            dfs(root.left, res)
            dfs(root.right, res)
            return res

        return dfs(p, []) == dfs(q, [])
