# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.check_min_depth(root)
    
    def check_min_depth(self, root):
        if not root.left and not root.right:
            return 1
        return min(self.check_min_depth(root.left), self.check_min_depth(root.right)) + 1