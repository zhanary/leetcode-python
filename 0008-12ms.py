class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        #去空格
        str = str.strip()
        if str == '':
            return 0
        
        #取符号
        sign = 1
        res = 0
        i = 0
        length = len(str)
        Max = (1 << 31) - 1
        
        if str[i] == '+':
            sign = 1
            i += 1
        elif str[i] == '-':   #避免越界不能直接if
            sign = -1
            i += 1
        
        #取数字
        for i in range(i, length):
            #非数字鉴别
            if str[i] < '0' or str[i] > '9':
                break
            res = res*10 + int(str[i])
        
        res = sign * res
        if res >= Max:
            return Max
        if res < Max * -1:
            return Max * -1 - 1 #最小要 -1
        
        return res
