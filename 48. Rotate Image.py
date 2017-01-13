class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        a1=[]
        a=0
        i=n-1
        for num in matrix:
            a1.extend(num)
        while i>=0:

            for x in range(0,n):
                matrix[x][i]=a1[a]
                a+=1
            i-=1
           
