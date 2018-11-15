class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return 0
        cursum = nums[0]
        maxsum = nums[0]
        
        for i in nums[1:]:
            cursum = max(i, cursum+i)  #取第i位之前的数字和与当前的i之间较大的一位
            maxsum = max(maxsum, cursum)  #取所有较大序列和中最大的一段
        
        return maxsum

