# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            q = head
            p = q.next
            while p:
                if p.val == q.val:
                    q.next = p.next
                    del p
                    p = q.next
                else:
                    q = q.next
                    p = q.next
        return head