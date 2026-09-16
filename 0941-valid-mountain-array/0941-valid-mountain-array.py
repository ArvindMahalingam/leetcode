class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        left=0
        n=len(arr)
        right=n-1
        if n==1:
            return  False
        while(arr[left]<arr[left+1] and (left+1)<n-1):
            left=left+1
        while(arr[right-1]>arr[right]):
            right-=1
        if left==right and left !=(n-1) and right !=0:
            return True
        return False
        