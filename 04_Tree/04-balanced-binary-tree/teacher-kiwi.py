from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def dfs(self, root: Optional[TreeNode], depth: int) -> int:
        if not root:
            return depth
        left_depth = depth
        right_depth = depth
        
        if root.left:
            left_depth = self.dfs(root.left, depth+1)
        if root.right:
            right_depth = self.dfs(root.right, depth+1)
        
        if abs(left_depth - right_depth) > 1:
            raise ValueError
        
        return max(left_depth, right_depth)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        try:
            self.dfs(root, 0)
            return True
        except:        
            return False