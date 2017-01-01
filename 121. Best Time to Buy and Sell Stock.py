class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
         #find max
                #find max
        if len(prices)==0:
            return(0)
        prices1=prices[:]#作用为完整复制一个list而不影响原list
        maxm=max(prices1)
        ccm=prices1.count(maxm)
        if ccm>1:
            for i in range(1,ccm):
                prices1.remove(maxm)
                print(prices1)
        while prices1.index(maxm)==0:
            prices1.remove(prices1[0])
            if len(prices1)==0:
                break
            maxm=max(prices1)
        if len(prices1)==0:
            return (0)
        else:
            maxloc=prices1.index(maxm)
            min1=min(prices1[0:maxloc])
            profit1=maxm-min1
        #find min
        prices2=prices[:]
        min2=min(prices2)
        minloc=prices2.index(min2)
        while minloc==len(prices2):
            prices2.pop(prices2[minloc])
        max2=max(prices2[minloc:len(prices2)+1])
        profit2=max2-min2
        if profit1<=0&profit2<=0:
            return (0)
        else:
            if profit1>profit2:
                return(profit1)
            if profit1<=profit2:
                return(profit2)
