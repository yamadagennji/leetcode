class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)-1):
            for x in range(i+1,len(nums)):
                vv=nums[i]+nums[x]
                if vv==target:
                    break
            if vv==target:
                break
        return (i,x)
