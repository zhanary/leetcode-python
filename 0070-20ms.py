# 类似于斐波那契
class Solution(object):
    def climbStairs(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        one_before = 2
        two_before = 1
        allsteps = 0
        
        for i in range(2, n):
            allsteps = one_before + two_before
            two_before = one_before
            one_before = allsteps
        
        return allsteps

