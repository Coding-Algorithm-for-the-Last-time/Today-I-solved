# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global count
        max_value = root.val
        count = 0

        def dfs(node, max_value):
            global count
            if node is None:
                return 0
            if node:
                if node.val >= max_value:
                    max_value = node.val
                    count += 1

            dfs(node.left, max_value)

            dfs(node.right, max_value)

        dfs(root, root.val)

        return count
