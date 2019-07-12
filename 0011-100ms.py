class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #双指针移动较小一个
        left = 0
        right = len(height) - 1 #注意
        res = 0
        tmp = 0
        while left < right:
            if height[left] < height[right]:
                tmp = height[left] * (right - left) #乘短的
                left += 1
            else:
                tmp = height[right] * (right - left)
                right -= 1
                
            res = max(res, tmp)
        
        return res
