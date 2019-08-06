class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        
        flag = 1   #存符号  
        rev = 0
        
        if x < 0:  #处理负号
            flag = -1
            x = -x
            
        while x > 0:
            rev = rev*10 + x%10 #巧
            x = x / 10
        
        rev = rev * flag
        
        if rev < - (1 << 31) or rev > (1 << 31) - 1:  #限制rev，审题
            return 0
        
        return rev

        
            
            
        
