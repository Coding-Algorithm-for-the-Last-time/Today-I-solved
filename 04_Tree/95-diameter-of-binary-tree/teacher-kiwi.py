from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    diameter = 0
    
    def dfs(self, node, depth):
            left_depth = depth
            right_depth = depth
            
            if node.left:
                left_depth = self.dfs(node.left, depth + 1)
            if node.right:
                right_depth = self.dfs(node.right, depth + 1)
            
            self.diameter = max(self.diameter, left_depth - depth + right_depth - depth)
            return max(left_depth, right_depth)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 0)
        return self.diameter