class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        target = 0
        out = []
        p = 0
        q = 0
        i = 0
        while i < len(nums)-2:
            target = 0 - nums[i]
            p = i + 1
            q = len(nums) - 1
            while p < q:
                if (nums[p] + nums[q]) == target :
                    out.append((nums[i], nums[p], nums[q]))
                    while p < len(nums)-1:
                        if nums[p] == nums[p+1]:
                            p = p + 1
                        else:
                            break
                    while q > 1:
                        if nums[q] == nums[q-1]:
                            q = q - 1
                        else:
                            break
                    p = p + 1
                    q = q - 1
                    
                elif (nums[p] + nums[q]) < target :
                    p = p + 1
                else :
                    q = q - 1
            while i < len(nums)-1:
                if nums[i] == nums[i+1]:
                    i = i + 1
                else:
                    i = i + 1
                    break   
        return out
