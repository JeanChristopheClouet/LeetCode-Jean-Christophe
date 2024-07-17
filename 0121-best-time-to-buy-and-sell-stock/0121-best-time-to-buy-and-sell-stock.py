class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maximum = 0
        l = 0
        r = 0

        while(r<len(prices)):
            if prices[r]>=prices[l]:
                profit = prices[r]-prices[l]
                maximum = max(profit, maximum)
                r+=1
            else:
                l+=1
        
        return maximum
        