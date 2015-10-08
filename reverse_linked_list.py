# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
      prev = None
      curr = head
      if not curr:
        return head
      while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
      return prev

l = ListNode(0)
s=Solution()
print s.reverseList(l)
