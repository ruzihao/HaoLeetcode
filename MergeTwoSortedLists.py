# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        h = ListNode(0)
        p = h
        while True:
            if not l1:
                p.next = l2
                break
            if not l2:
                p.next = l1
                break
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        return h.next

l1 = ListNode(1)
l1.next = ListNode(4)
l2 = ListNode(2)
l2.next = ListNode(3)
l = Solution().mergeTwoLists(l1, l2)
p = l
while p:
    print p.val
    p = p.next

