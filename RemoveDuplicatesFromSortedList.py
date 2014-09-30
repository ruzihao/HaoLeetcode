# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def deleteDuplicates(self, head):
		q = head
		if q and q.next:
			p = q.next
			while p:
				if q.val == p.val:
					p = p.next
					del q.next
					q.next = p
				else:
					p = p.next
					q = q.next
		return head

head = ListNode(2)
head.next = ListNode(2)
head.next.next = ListNode(2)
p = Solution().deleteDuplicates(head)

while p:
	print p.val
	p = p.next
