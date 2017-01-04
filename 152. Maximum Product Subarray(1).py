class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        abc=[]
        aa=1
        if len(nums)==1:
            return (nums[0])
        else:
            for i in range(0,len(nums)):
                bb=1
                for m in range(0,i+1):
                    if nums[i]-nums[i-m]==m:
                        bb=bb*nums[i-m]
                        if bb>aa:
                            aa=bb
                    else:
                        if bb>aa:
                            aa=bb
                            bb=1
                            break
                    
                    
        return (aa)        
