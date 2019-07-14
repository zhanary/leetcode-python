class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rom = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L','XL', 'X', 'IX', 'V', 'IV', 'I')
        dig = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1) 
        res = ''
        
        for r, d in zip(rom, dig):
            res += r * (num // d)
            num %= d
        return res
        
