from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.tree_list(p) == self.tree_list(q)

    def tree_list(self, tree: Optional[TreeNode]) -> list:
        res = []
        trees = deque()
        trees.append(tree)

        while trees:
            tree = trees.popleft()
            res.append(None if not tree else tree.val)
            if tree and (tree.left or tree.right):
                trees.append(tree.left or None)
                trees.append(tree.right or None)
            
        return res