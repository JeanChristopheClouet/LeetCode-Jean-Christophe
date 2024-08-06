class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        map = {}

        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num]+=1
        
        for key in map:
            if map[key]>1:
                return True
        
        return False
        