class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #避免越界
        if numRows <= 1 or len(s) < numRows:
            return s
        
        #建立空矩阵
        res = [''] * numRows
        
        #读入数据
        for i in range(len(s)):
            tmp = i % (2*numRows - 2)   #一组为2numRows-2
            if tmp < numRows:
                res[tmp] += s[i]
            else:
                tmp = 2*numRows - 2 - tmp
                res[tmp] += s[i]
        return ''.join(res)
        
        
