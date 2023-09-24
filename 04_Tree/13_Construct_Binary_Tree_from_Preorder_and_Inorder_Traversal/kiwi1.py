# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder:
            return None

        tree = TreeNode(preorder.pop(0))

        def append_tree(root, inorder) -> None:
            if not preorder:
                return

            root_id = inorder.index(root.val)
            left = inorder[:root_id]
            right = inorder[root_id + 1 :]

            if left:
                left_node = TreeNode(preorder.pop(0))
                root.left = left_node
                append_tree(left_node, left)

            if right:
                right_node = TreeNode(preorder.pop(0))
                root.right = right_node
                append_tree(right_node, right)

        append_tree(tree, inorder)

        return tree
