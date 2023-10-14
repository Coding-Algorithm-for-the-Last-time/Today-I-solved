from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        nodes = []

        def dfs(node: TreeNode | None):
            if node:
                nodes.append(node.val)
                dfs(node.left)
                dfs(node.right)
            else:
                nodes.append(None)

        dfs(root)
        return ",".join(map(str, nodes))

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = deque(data.split(","))
        root = TreeNode(nodes.popleft())
        if not nodes:
            return None

        def dfs(root: TreeNode | None):
            if root:
                if nodes:
                    value = nodes.popleft()
                    if value != "None":
                        root.left = TreeNode(int(value))
                    dfs(root.left)
                if nodes:
                    value = nodes.popleft()
                    if value != "None":
                        root.right = TreeNode(int(value))
                    dfs(root.right)

        dfs(root)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
