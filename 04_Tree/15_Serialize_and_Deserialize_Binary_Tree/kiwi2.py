from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    nodes = deque()

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def dfs(node: TreeNode | None):
            if node:
                self.nodes.append(node.val)
                dfs(node.left)
                dfs(node.right)
            else:
                self.nodes.append(None)

        dfs(root)
        return ""

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs():
            val = self.nodes.popleft()
            if val == None:
                return None
            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
