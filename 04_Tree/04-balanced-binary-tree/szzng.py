# https://leetcode.com/problems/balanced-binary-tree/submissions/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = True

    def depth(self, node):
        if node is None: return 0

        left = self.depth(node.left)
        right = self.depth(node.right)

        if abs(left - right) > 1: self.result = False

        return max(left, right) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.depth(root)
        return self.result
