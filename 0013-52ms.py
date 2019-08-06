class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        i = len(s) - 2
        sum = val[s[-1]]

        while i >= 0:
            if val[s[i]] >= val[s[i+1]]:
                sum = sum + val[s[i]]
                i = i - 1
            else:
                sum = sum - val[s[i]]
                i = i - 1
        return sum
