class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        global aa
        if len(triangle)==1:
            cc=triangle[0]
            return (cc[0])
        else:
            for i in range(1,len(triangle)):
                aa=triangle[i]
                bb=triangle[i-1]
                aa[0]=aa[0]+bb[0]
                aa[len(aa)-1]=bb[len(bb)-1]+aa[len(aa)-1]
                for x in range(1,len(aa)-1):
                    aa[x]=min(aa[x]+bb[x-1],aa[x]+bb[x])
            cc=min(triangle[len(triangle)-1])
            return (cc)
