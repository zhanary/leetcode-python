class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        output = 0
        dic = {}
        start = 0
        
        for i, j in enumerate(s):
            if j in dic and dic[j] >= start:
                num = i - start
                output = num if num > output else output
                start = dic[j] + 1
            dic[j] = i
        num = len(s) - start #防止输入0
        return num if num > output else output
            

            
            
