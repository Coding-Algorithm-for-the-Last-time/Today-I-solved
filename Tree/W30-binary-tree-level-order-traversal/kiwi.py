from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        trees_queue = deque()
        res = []
        if root:
            trees_queue.append([root])
            res.append([root.val])
        while trees_queue:
            temp = []
            for tree in trees_queue.popleft():
                if tree.left:
                    temp.append(tree.left)
                if tree.right:
                    temp.append(tree.right)
            if temp:
                trees_queue.append(temp)
                res.append([tree.val for tree in temp])
        return res
