class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        elements = {}
        output = []

        for i in nums:
            if i in elements:
                new_value = elements.get(i)+1
                elements[i]=new_value
            else:
                elements[i]=1

        for i in range(k):
            frequentest = max(elements, key=elements.get)
            output.append(frequentest)
            elements.pop(frequentest)
            

            
        return output