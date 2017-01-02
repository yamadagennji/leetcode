#this is my way
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        if len(nums)==0:
            return(0)
        #非空集合
        while i+1<len(nums):
            if nums[i]==nums[i+1]:
                nums.remove(nums[i])
            else:
                i=i+1
        return (len(nums))
        
#this is a top solution
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1
