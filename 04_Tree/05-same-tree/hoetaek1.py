from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_tree = []
        q_tree = []

        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        def dfs(node, tree, depth=0):
            if node.left:
                dfs(node.left, tree, depth=depth + 1)
            else:
                tree.append(None)
            if node.right:
                dfs(node.right, tree, depth=depth + 1)
            tree.append(node.val)

        dfs(p, p_tree)
        dfs(q, q_tree)

        return p_tree == q_tree
