# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
	def max_depth(self, root):
		if root==None:
			return 0
		return 1+max(self.max_depth(root.left), self.max_depth(root.right))

	def check_root(self, root):
		if root==None:
			return True
		elif abs(self.max_depth(root.left)-self.max_depth(root.right))>1:
			return False
		else:
			return self.check_root(root.left) and self.check_root(root.right)
	
	def isBalanced(self, root):
		return self.check_root(root)

t = TreeNode(1)
t.left = TreeNode(2)
#t.left.left = TreeNode(3)
print Solution().isBalanced(t)
