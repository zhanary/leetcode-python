# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        res = ListNode(0) #result
        res.next = head #指向head
        tmp = res #操作tmp
        
        for i in range(0, n):
            head = head.next
            
        while head != None:
            head = head.next
            tmp = tmp.next
        tmp.next = tmp.next.next
        
        return res.next
        
