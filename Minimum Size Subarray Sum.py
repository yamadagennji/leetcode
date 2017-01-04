class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums)<s:
            return(0)
        else:
            aa=0
            total=0
            sol=len(nums)+1
            for bb,j in enumerate(nums):
                total+=j
                while total>=s:
                    sol=min(sol,bb-aa+1)
                    total-=nums[aa]
                    aa+=1
                    
            
            return sol
                
            
