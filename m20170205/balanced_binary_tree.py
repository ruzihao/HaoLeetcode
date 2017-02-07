# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        is_bt, _ = self.check_height(root)
        return is_bt
    
    def check_height(self, root):
        if not root:
            return True, 0
        is_bt_left, height_left = self.check_height(root.left)
        is_bt_right, height_right = self.check_height(root.right)
        return is_bt_left and is_bt_right and abs(height_left-height_right)<=1, max(height_left, height_right)+1