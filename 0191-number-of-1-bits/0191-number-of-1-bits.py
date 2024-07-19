class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0
        
        while(n!=0):
            quotient = int(n/2)
            if float(quotient) == float(n)/float(2):
                remainder = 0
                count+=remainder
            else:
                remainder = 1
                count+=remainder
            n=quotient
        
        return count