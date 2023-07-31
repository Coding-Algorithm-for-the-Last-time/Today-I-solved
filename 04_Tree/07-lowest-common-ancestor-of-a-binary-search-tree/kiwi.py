# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root
        
        if (root.val > p.val) is not (root.val > q.val):
            return root

        child_node = root.left if root.val > p.val else root.right
        return self.lowestCommonAncestor(child_node, p, q)