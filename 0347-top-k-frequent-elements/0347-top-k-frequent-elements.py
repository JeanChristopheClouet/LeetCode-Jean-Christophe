class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        maxes = []
        elements = {}

        for i in nums:
            if i in elements:
                elements[i]+=1
            else:
                elements[i]=1

        for _ in range(k):
            m = max(nums, key=elements.get)
            maxes.append(m)
            elements.pop(m)

        return maxes 


        