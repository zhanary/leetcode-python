# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        def covert(left, right):
            if left > right:
                return None
            mid = (left + right) / 2
            root = TreeNode(nums[mid])
            root.left = covert(left, mid-1)
            root.right = covert(mid+1, right)
            return root
        return covert(0, len(nums)-1)
