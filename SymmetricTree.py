# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def isSymmetric(self, root):
		if root==None:
			return True
		else:
			return self.isMirror(root.left, root.right)

	def isMirror(self, l, r):
		if l==None and r==None:
			return True
		elif l==None or r==None:
			return False
		else:
			if l.val!=r.val:
				return False
			else:
				return self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left)

	def isSame(self, left, right):
		if left==None and right==None:
			return True
		elif (left!=None and right==None) or (left==None and right!=None):
			return False
		else:
			if left.left==None and left.right==None and right.left==None and right.right==None:
				if left.val==right.val:
					return True
				else:
					return False
			else:
				return self.isSame(left.left, right.left) and self.isSame(left.right, right.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
print Solution().isSymmetric(root)
