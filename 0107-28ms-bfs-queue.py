# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        # with bfs queue
        queue = collections.deque([(root, 0)])#双端队列
        value = []
        
        while queue:
            node, level = queue.popleft()
            if node:
                if len(value) < level + 1:
                    value.insert(0, [])
                value[-(level+1)].append(node.val)
                queue.append((node.left, level+1))   
                queue.append((node.right, level+1))
        
        return value
