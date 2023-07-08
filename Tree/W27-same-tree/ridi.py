from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


## 회택이 풀이 공부
class Solution2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def dfs(root, res=[]):
            if not root:
                res.append(None)
                return
            res.append(root.val)
            dfs(root.left, res)
            dfs(root.right, res)
            return res
        
        return dfs(p, []) == dfs(q, [])


## 승희 풀이 공부
class Solution3:
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
