class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        position=0
        if target>nums[(len(nums)-1)]:
            position=len(nums)
        for i in range(len(nums)):
            
            if nums[i]==target:
        
                position=i
                break
            elif nums[i]>target:
                position=i
                break

        return position