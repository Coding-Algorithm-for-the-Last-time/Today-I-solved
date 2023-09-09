# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        cnt = [0]
        res = [0]

        def dfs(node):
            if node.left:
                dfs(node.left)

            cnt[0] += 1
            if cnt[0] == k:
                res[0] = node.val
                raise Exception

            if node.right:
                dfs(node.right)

        try:
            dfs(root)
        except:
            return res[0]
