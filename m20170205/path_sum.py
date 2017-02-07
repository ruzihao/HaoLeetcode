# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.check_sum(root, sum)
    
    def check_sum(self, root, s):
        if s<0:
            return False
        if not root:
            return s==0
        return self.check_sum(root.left, s-root.val) or self.check_sum(root.right, s-root.val)