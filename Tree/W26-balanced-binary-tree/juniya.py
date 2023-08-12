class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth=0):
            left_d = depth
            right_d = depth
            if node.left:
                left_d = dfs(node.left, depth+1)
            if node.right:
                right_d = dfs(node.right, depth+1)
            return left_d, right_d

        dfs(root)


root = [1, 2, 3, 4, 5]
