class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #try DP
        n = len(s)    #length of string
        maxlenth = 0 
        maxstart_Index = 0
        
        dp = [([False] * n) for i in range (n)]  #n * n false array
        
        for i in range(n):    #对角线为1
            dp[i][i] = True
            maxlenth = 1
            maxstart_Index = i
        
        for i in range(n - 1):    # 两个相邻的相等
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                maxlenth = 2
                maxstart_Index = i
                
        for curLen in range(3, n + 1):
            for start_Index in range(n - curLen + 1):
                end_Index = start_Index + curLen - 1
                dp[start_Index][end_Index] = (dp[start_Index + 1][end_Index - 1] and s[start_Index] == s[end_Index])
                if dp[start_Index][end_Index] == True and curLen > maxlenth:
                    maxlenth = curLen
                    maxstart_Index = start_Index
        
        return s[maxstart_Index:maxstart_Index + maxlenth]
