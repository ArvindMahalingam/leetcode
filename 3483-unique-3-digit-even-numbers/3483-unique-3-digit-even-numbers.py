class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        array=[0]*10
        for d in digits:
            array[d]+=1
        res=0
        for number in range(100,1000,2):
            digit1=number//100
            digit2=(number//10)%10
            digit3=number%10
            array[digit1]-=1
            array[digit2]-=1
            array[digit3]-=1
            if array[digit1]>=0 and array[digit2]>=0 and array[digit3]>=0:
                res+=1
            array[digit1]+=1
            array[digit2]+=1
            array[digit3]+=1
        return res
            
        
        