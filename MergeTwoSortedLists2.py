# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        # if L1 empty
        if l1 is None:
            return l2
        # elif L2 empty
        elif l2 is None:
            return l1
        # else
        else:
            # if L1.val =< L2.val
            if l1.val <= l2.val:
                # head = L1
                head = l1
                # r = L1
                r = l1
                # p = r.next
                p = r.next
                # q = L2
                q = l2
            # else
            else:
                # head = L2
                head = l2
                # r = L2
                r = l2
                # p = r.next
                p = r.next
                # q = L1
                q = l1
            # while p q not null
            while p is not None and q is not None:
                # if p.val <= q.val
                if p.val > q.val:
                    # r 
                    r.next = q
                    q = q.next
                    r = r.next
                    r.next = p
                # else
                else:
                    r = p
                    p = r.next
            # if p null
            if p is None:
                r.next = q
            return head


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(8)
l.next.next.next = None
r = ListNode(1)
r.next = ListNode(5)
r.next.next = ListNode(5)
r.next.next.next = None
def prnt(x):
    while x:
        print x.val
        x = x.next
prnt(Solution().mergeTwoLists(l,r))