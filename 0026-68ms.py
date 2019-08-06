class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        
        index = 1
        for i in nums[1:]:
            if i != nums[index-1]:   #如果不相等
                nums[index] = i    #当前nums[i]填入index表中
                index = index + 1

        return index
        
