class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        profits=[]
        
        while(right<len(prices)):
            if(prices[right]>=prices[left]):
                profit = prices[right]-prices[left]
                right+=1
                profits.append(profit)
            else:
                left+=1
        return max(profits) 