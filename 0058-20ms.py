class Solution(object):
    def lengthOfLastWord(self, s):
        if not s:
            return 0
        
        count = 0
        #rstrip是删除字符串末尾的字符
        #split是分割字符串
        count = len(s.rstrip(' ').split(' ')[-1])
        return count
