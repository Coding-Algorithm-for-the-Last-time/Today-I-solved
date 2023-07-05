# https://leetcode.com/problems/same-tree/description/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def isSameNode(self, n1, n2):
        if n1 is None and n2 is None:
            return True

        if n1 is None or n2 is None or n1.val != n2.val:
            return False

        return self.isSameNode(n1.left, n2.left) and self.isSameNode(n1.right, n2.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.isSameNode(p, q)


class Solution2:
    def __init__(self):
        self.pq = []
        self.qq = []

    def check_node(self, queue):
        node = queue.pop(0)
        if node is None: return
        queue.append(node.left)
        queue.append(node.right)
        return node.val

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.pq, self.qq = [p], [q]

        while len(self.pq) != 0 or len(self.qq) != 0:
            if self.check_node(self.pq) != self.check_node(self.qq):
                return False

        return len(self.pq) == 0 and len(self.qq) == 0


class Solution3:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return str(p) == str(q)
