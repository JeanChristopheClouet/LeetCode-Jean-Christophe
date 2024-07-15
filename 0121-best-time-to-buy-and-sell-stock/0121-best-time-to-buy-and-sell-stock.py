class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits = []
        l =0
        r = 0

        while(r<len(prices)):
            if prices[l]<=prices[r]:
                
	            profits.append(prices[r]-prices[l])
	            r+=1
            else:
                l+=1
        
        return max(profits)