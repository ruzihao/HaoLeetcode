# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
		s = ListNode(0)
		p, p1, p2 = s, l1, l2
		carry = 0
		while p1 or p2:
			if p1 and p2:
				ss = p.val + p1.val + p2.val
				p1 = p1.next
				p2 = p2.next
			elif not p1 and p2:
				ss = p.val + p2.val
				p2 = p2.next
			elif p1 and not p2:
				ss = p.val + p1.val
				p1 = p1.next
			carry = ss//10
			p.val = ss%10
			if carry or p1 or p2:
				p.next = ListNode(carry)
				p = p.next
		return s

def main():
	l1 = ListNode(9)
	l1.next = ListNode(9)
	l2 = ListNode(9)
	# l2.next = ListNode(5)
	s = Solution().addTwoNumbers(l1, l2)
	p = s
	while p:
		print p.val
		p = p.next

if __name__ == '__main__':
	main()
