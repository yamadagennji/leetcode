def thirdMax(nums):
        if len(nums) < 3:
            return max(nums)
        a1=nums
        a2=[]
        for i in a1:
            if not i in a2:
                a2.append(i)
        a2.remove(max(a2))
        a2.remove(max(a2))
        return max(a2)
a=thirdMax([1,2,3,4,5,3,3,3,3,5,5,5,5])
print (a)
