# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def maxDepth(self, root):
		if root==None:
			return 0
		return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.right = TreeNode(4)
print Solution().maxDepth(root)

