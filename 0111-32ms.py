# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        next_node = deque()
        cur = (1, root) #深度，当前位置
        while(cur[1].left or cur[1].right):
            if cur[1].left != None:
                next_node.append((cur[0]+1, cur[1].left))   #深度+1，存下节点
            if cur[1].right != None:
                next_node.append((cur[0]+1, cur[1].right))
            cur = next_node.popleft() #cur指向下一个
            
        return cur[0]
