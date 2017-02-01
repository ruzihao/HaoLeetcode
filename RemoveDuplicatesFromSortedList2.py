# 19Nov2014

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
        if not head:
            return head
        else:
            p = q.next
            while p:
                if p.val == q.val:
                    p = p.next
                    del q.next
                    q.next = p
                else:
                    p = p.next
                    q = q.next
            return head

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
p = Solution().deleteDuplicates(head)
while p:
    print p.val
    p = p.next