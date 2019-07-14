class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()    #先排序
        
        ans = None  #当前最优

        for i in range(len(nums)):
            left = i + 1        #数字i的右边
            right = len(nums) - 1
            
            while left < right:   #非常重要防止越界
                thsum = nums[i] + nums[left] + nums[right]   #总和            
                
                if ans == None or abs(thsum - target) < abs(ans - target): #更好的sum值更新
                    ans = thsum 

                if thsum > target:
                    right -= 1
                elif thsum < target:
                    left +=1
                else:
                    return target
            
        return ans
                
