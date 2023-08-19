# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = [True]

        def dfs(node, minValue, maxValue):
            if not node:
                return minValue, maxValue

            LminValue, LmaxValue = dfs(node.left, minValue, maxValue)
            RminValue, RmaxValue = dfs(node.right, minValue, maxValue)

            minValue = min(LminValue, RminValue, node.val)
            maxValue = max(LmaxValue, RmaxValue, node.val)

            if node.val <= LmaxValue:
                res[0] = False
            if node.val >= RminValue:
                res[0] = False

            return minValue, maxValue

        dfs(root, 2**32, -(2**32))

        return res[0]
