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
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

root = TreeNode(0)
l1 = TreeNode(0)
l2 = TreeNode(0)
l3 = TreeNode(0)
r1 = TreeNode(0)
root.left = l1
# l1.right = l2
# l2.left = l3
# root.right = r1

print Solution().maxDepth(None)
print Solution().maxDepth(root)