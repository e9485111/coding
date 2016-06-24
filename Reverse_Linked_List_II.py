 class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        first = dummy
        for i in range(0,m):
            pre = first
            first = first.next
        last = first
        for i in range(0,n-m):
            last = last.next
        tmp = last.next
        last.next = None
        last = tmp

        p = None
        while first:
            tmp = first.next
            first.next = p
            p = first
            first = tmp

        pre.next = p
        while p.next:
            p = p.next
        p.next = last
        return dummy.next






