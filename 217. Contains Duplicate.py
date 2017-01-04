#方法1
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        i=0
        while i<len(nums):
            aa=nums.count(nums[i])
            if aa>1:
                return True
                break
            i+=1
        return False
        
#方法2
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(0,len(nums)-1):
            aa=nums[i+1]-nums[i]
            if aa==0:
                return True
                break
        return False
