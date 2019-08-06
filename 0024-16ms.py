# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        out = ListNode(0)
        out.next = head
        result = out
        while out.next:
            if out.next.next:
                p = out.next
                q = out.next.next.next
                out.next = out.next.next
                out.next.next = p
                p.next = q
                out = p
            else:
                break
        return result.next
                
                

        
