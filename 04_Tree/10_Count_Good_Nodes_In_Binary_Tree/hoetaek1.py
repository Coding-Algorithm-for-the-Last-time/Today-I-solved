# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(maxValue, node):
            if maxValue <= node.val:
                maxValue = node.val
                self.res += 1

            if node.left:
                dfs(maxValue, node.left)
            if node.right:
                dfs(maxValue, node.right)

        dfs(root.val, root)
        return self.res
