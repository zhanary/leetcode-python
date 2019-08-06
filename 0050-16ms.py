class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        ans = 1
        tmp = x
        
        while n != 0:
            if n % 2 != 0:
                ans = ans * tmp
            tmp = tmp * tmp
            
            n = n // 2           
        return ans
            
        
        
