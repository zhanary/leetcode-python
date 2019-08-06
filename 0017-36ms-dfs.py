letter = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:    #空
            return []

        result = []
        l = len(digits)
        self.dfs(digits, 0, '', result, l)
        return result
        
    def dfs(self, digits, index, string, result, l):
        if index == l:
            result.append(string)
            return
        
        for t in letter[digits[index]]: ##每个字母
            self.dfs(digits, index+1, string+t, result, l)
