class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        output = []
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1

        for _ in range(k):
            f = max(d, key=d.get)
            output.append(f)
            d.pop(f)
        
        return output 