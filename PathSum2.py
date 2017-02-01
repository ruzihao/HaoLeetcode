# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, ssum):
        return bool(root) & self.check_sum(root, 0, ssum)

    def check_sum(self, node, cur, ssum):
        if node is None:
            return False
        if node.left is None and node.right is None:
            if cur + node.val == ssum:
                return True
            else:
                return False
        else:
            return self.check_sum(node.left, cur + node.val, ssum) | self.check_sum(node.right, cur + node.val, ssum)

root = TreeNode(1)
root.left = TreeNode(2)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(2)

print Solution().hasPathSum(root, 1)