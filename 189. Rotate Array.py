#read the example carefully
#top solution
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
        
#my solution
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k==0:
            a=1
        else:
            for i in range(0,k):
                nums.insert(0,nums[len(nums)-1])#insert才能往最前面放
                print(nums)
                nums.pop(len(nums)-1)
                print(nums)
                
