class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cc=nums.count(0)
        if cc>0:
            for i in range(1,cc+1):
                nums.remove(0)
                nums.append(0)
