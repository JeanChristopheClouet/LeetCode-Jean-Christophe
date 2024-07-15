class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        o = []
        e = {}

        for i in nums:
            if i in e:
                e[i]+=1
            else:
                e[i]=1
        
        for _ in range(k):
            f = max(e, key=e.get)
            o.append(f)
            e.pop(f)
        
        return o
