# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        # with dfs recursivrly
        value = []
        self.dfs(root, 0, value)
        return value
        
    def dfs(self, root, level, value):
        if root:
            if len(value) < level + 1:
                value.insert(0, [])
                
            value[-(level+1)].append(root.val)
            self.dfs(root.left, level+1, value)
            self.dfs(root.right, level+1, value)
