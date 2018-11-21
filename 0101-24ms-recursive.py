# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        else: 
            return self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            outpair = self.isMirror(left.left, right.right)
            inpair = self.isMirror(left.right, right.left)
            return outpair and inpair
        
        return False      

