class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(list(set(candidates)))
        results = []
        self.dfs(candidates, target, [], 0, results)
        return results
    
    def dfs(self, candidates, target, comlist, start, results):
        if target == 0:
            return results.append(list(comlist))
        
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return
            
            comlist.append(candidates[i])
            self.dfs(candidates, target - candidates[i], comlist, i, results)
            
            comlist.pop()

        
    
        
