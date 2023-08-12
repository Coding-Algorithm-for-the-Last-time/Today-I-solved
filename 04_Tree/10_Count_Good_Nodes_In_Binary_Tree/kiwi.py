# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]

        def dfs(node: TreeNode, _max: int):
            if node:
                if node.val >= _max:
                    res[0] += 1
                dfs(node.left, max(_max, node.val))
                dfs(node.right, max(_max, node.val))

        dfs(root, float("-inf"))
        return res[0]
