class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        from itertools import combinations
        aa=list(combinations([1, 2, 3,4,5,6,7,8,9], k))
        abc=[]
        for i in aa:
            if sum(i) ==n:
                abc.append(i)
        return(abc)
