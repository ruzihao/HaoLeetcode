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
		if ssum==0:
			return True
		elif ssum<0 or root==None:
			return False
		return self.hasPathSum(root.left, ssum-root.val) or self.hasPathSum(root.right, ssum-root.val)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.right = TreeNode(4)
print Solution().hasPathSum(root, 6)
