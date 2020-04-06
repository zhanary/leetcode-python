class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.lenmax = ''
        for i in range(len(s)):
            self.findmax(s, i, i)
            self.findmax(s, i, i+1)
        return self.lenmax

    def findmax(self, s, left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        left += 1

        if (right - left) > len(self.lenmax):
            self.lenmax = s[left:right]
