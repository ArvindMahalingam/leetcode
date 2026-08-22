class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res=[]
       
        i=len(num1)-1
        j=len(num2)-1
        carry=0
        while i>=0 or j>=0 or carry:
            if i>=0:
                value1=ord(num1[i])-ord('0')
            else:
                value1=0
            if j>=0:
                value2=ord(num2[j])-ord('0')
            else:
                value2=0
            
            colum_sum=value1+value2+carry
            carry=colum_sum//10
            digit_sum=colum_sum%10
            
            res.append(digit_sum)
            i-=1
            j-=1
        res=res[::-1]
        ans=""
        for i in res:
            ans=ans+str(i)
        return ans

        