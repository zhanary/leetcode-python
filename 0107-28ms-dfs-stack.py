# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        # with dfs stackd
        stack = [(root, 0)]
        value = []
        
        while stack:
            node, level = stack.pop()
            if node:
                if len(value) < level + 1:
                    value.insert(0, [])
                value[-(level+1)].append(node.val)
                
                stack.append((node.right, level+1))   #先进去的后出来
                stack.append((node.left, level+1))
        
        return value
