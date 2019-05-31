#格雷码本质是 i XOR i//2
#当n=2
#i = 0, 1, 2, 3
#i=0, 0^0 -> 00 ^ 00 = 00 -> 0
#i=1, 1^0 -> 01 ^ 00 = 01 -> 1
#i=2, 2^1 -> 10 ^ 01 = 11 -> 3
#i=3, 3^1 -> 11 ^ 01 = 10 -> 2 

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        if n == 0:
            return [0]
        for i in range(2**n):
            result.append(i^(i//2))
        return result
