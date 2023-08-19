# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.valid(root, float("-inf"), float("inf"))

    def valid(self, node, l, r):
        if not node:
            return True
        if not l < node.val < r:
            return False
        return self.valid(node.left, l, node.val) and self.valid(
            node.right, node.val, r
        )
