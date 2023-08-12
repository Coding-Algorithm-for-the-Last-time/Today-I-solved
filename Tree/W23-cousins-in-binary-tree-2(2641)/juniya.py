
root = [5, 4, 9, 1, 10, None, 7]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


parent = {}
depth = {}


def dfs(node, par=None):
    if node:
        parent[node.val] = par
        depth[node.val] = 1 + depth[par] if par else 0
        dfs(node.left, node.val)
        dfs(node.right, node.val)


print(dfs(root))
