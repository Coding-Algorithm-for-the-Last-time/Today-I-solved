# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node, depth=0):
            left_d = depth
            right_d = depth
            if node.left:
                left_d = dfs(node.left, depth+1)
            if node.right:
                right_d = dfs(node.right, depth+1)
            return left_d, right_d

        if dfs(p) == dfs(q):
            return True

        else:
            return False
