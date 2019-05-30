#非常精巧的方法，比较的是长度

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res =""
        for i in range(len(s)):
            res = max(self.longest(s, i, i), self.longest(s, i, i+1), res, key=len) #比较长度
        return res
    
    def longest(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:   #左减右加，比较是否相等
            l -= 1
            r += 1
        return s[l+1:r]
