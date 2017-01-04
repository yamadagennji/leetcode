class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a=0
        for i in range(0,len(digits)):
            if digits[i]-9!=0:
                a+=1
        if a==0:
            for i in range(0,len(digits)):
                digits[i]=0
            digits.insert(0,1)
        else: 
            if  digits[len(digits)-1]==9:
                 for x in range(1,len(digits)):
                     digits[len(digits)-x]=0
                     if digits[len(digits)-x-1]+1!=10:
                         digits[len(digits)-x-1]= digits[len(digits)-x-1]+1
                         break
                     
            else:
                digits[len(digits)-1]=digits[len(digits)-1]+1
        return(digits)

    
    
#别璐莎的方法    
    class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        b=''.join([str(i) for i in digits])
        type(b)
        c=int(b)
        d=c+1
        e=str(d)
        f=list(e)
        g=[]
        for i in f:
            g.append(int(i))
        return(g)
