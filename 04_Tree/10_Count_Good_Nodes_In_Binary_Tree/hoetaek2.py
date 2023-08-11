# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(maxValue, node):
            if not node:
                return 0

            if maxValue <= node.val:
                maxValue = node.val
                res = 1
            else:
                res = 0

            res += dfs(maxValue, node.left)
            res += dfs(maxValue, node.right)

            return res

        return dfs(root.val, root)
