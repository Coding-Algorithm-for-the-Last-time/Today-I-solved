/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function (root, subRoot) {
  const isEqual = (node1, node2) => {
    if (!node1 || !node2) return !node1 && !node2;
    if (node1.val !== node2.val) return false;
    return isEqual(node1.left, node2.left) && isEqual(node1.right, node2.right);
  };

  const dfs = (node) => {
    if (!node) return false;
    if (isEqual(node, subRoot)) return true;
    return dfs(node.left) || dfs(node.right);
  };

  return dfs(root);
};
