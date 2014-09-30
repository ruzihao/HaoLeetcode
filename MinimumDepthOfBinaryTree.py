# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return an integer
	def minDepth(self, root):
		if root==None:
			return 0
		elif root.left and not root.right:
			return self.minDepth(root.left)+1
		elif not root.left and root.right:
			return self.minDepth(root.right)+1
		return min(self.minDepth(root.left), self.minDepth(root.right))+1

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
#root.right = TreeNode(4)
print Solution().minDepth(root)


