class Solution(object):
    def majorityElement(self,nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        elements=[]
        nums2=set(nums)
        for i in nums2:
            aa=nums.count(i)
            if aa>(len(nums)/3):
               elements.append(i)
        return elements
