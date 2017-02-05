# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            p = ListNode(0)
            import pdb; pdb.set_trace()
            p.next, q = l1, l2
            r = p.next
            while r and q:
                if r.val <= q.val:
                    p.next = r
                    r = p.next
                else:
                    p.next = q
                    q = q.next
                    p = q
            if not r:
                p.next = q
        return l1
                    
Solution().mergeTwoLists(ListNode(1), ListNode(2))
