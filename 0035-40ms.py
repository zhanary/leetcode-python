class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l0 = 0
        l1 = len(nums) - 1
        while l0 < l1:
            mid = (l0 + l1)/2
            if nums[mid] >= target:
                l1 = mid
            else:
                l0 = mid + 1
                
        if l0 == len(nums) - 1 and nums[l0] < target:
            l0 += 1
        
        return l0
