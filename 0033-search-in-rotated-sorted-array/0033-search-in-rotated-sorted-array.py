class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


        index = -1
        n = len(nums)

        if nums[0]==target:
            return 0
        elif nums[n-1]==target:
            return n-1

        if nums[0]<nums[n-1]:
            for k in range(len(nums)):
                if nums[k]==target:
                    return k
         
        if nums[0]-target>=nums[n-1]-target:
            i=0

            while i<n:
                if nums[i]==target:
                    return i
                i+=1

        else:
            j=n-1

            while j<0:
                
                if nums[j]==target:
                    return j
                j-=1
            
                
        
        return index

