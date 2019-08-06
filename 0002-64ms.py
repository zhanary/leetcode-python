# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #先申请一个新的list
        head = ListNode(0)
        ptr = head
        
        output = 0
        
        while True:
            if l1 is not None:
                output += l1.val
                l1 = l1.next
            if l2 is not None:
                output += l2.val
                l2 = l2.next
                
            ptr.val = output % 10
            output = output / 10
            
            if l1 != None or l2 != None or output != 0:
                ptr.next = ListNode(0)
                ptr = ptr.next
            else:
                break
        
        return head
