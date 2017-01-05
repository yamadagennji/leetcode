class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices.append(0)
        print(prices)
        print(len(prices))
        if len(prices)==1:
            return 0
        elif len(prices)==2:
            return 0
        
        else:
            i=0
            j=0
            profit=0
            while i<len(prices)-1:
                if prices[i+1]<prices[i]:
                    profit+=prices[i]-prices[j]
                    j=i+1
                i+=1
        return (profit)
