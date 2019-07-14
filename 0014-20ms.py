class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #字符串长度0或者无字符串
        if len(strs) == 0 or not strs:
            return ''
        
        for i in range(len(strs[0])):    #以第一个为基准
            for j in range(len(strs)):     #比较每一个子str
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:  #越位或者不等
                    return strs[0][0:i]    #返回当前比较位之前
        return strs[0]
    
