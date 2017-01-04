class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
    
        dic = {}
        for i, num in enumerate(numbers):#遍历所有元素，i代表下角标，num代表数字
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i#将num保存在i位置上
        
        
