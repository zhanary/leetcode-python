#检测树是否对称，递归方法很优雅

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.judge(root.left, root.right)
    
    def judge(self, l, r):
        if not l and not r:
            return True
        if l and not r:
            return False
        if r and not l:
            return False
        if r.val != l.val:
            return False
        return self.judge(l.left, r.right) and self.judge(l.right, r.left)
