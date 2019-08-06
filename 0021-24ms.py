# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        l3 = None
        
        if l1.val <= l2.val :
            l3 = l1
            l1 = l1.next
        else :
            l3 = l2
            l2 = l2.next
            
        out = l3
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else :
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        if l1 is None:
            l3.next = l2
        else:
            l3.next = l1
        
        return out
            
                
        
