# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        try:
            self.min_max(root)
        except:
            return False
        return True

    def min_max(self, root):
        if not root:
            return (float("inf"), float("-inf"))
        l_min, l_max = self.min_max(root.left)
        r_min, r_max = self.min_max(root.right)

        if not l_max < root.val < r_min:
            raise Exception

        return (min(l_min, root.val, r_min), max(l_max, root.val, r_max))
