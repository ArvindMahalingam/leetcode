class Solution(object):
    def findMin(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        n=len(arr)
        right=n-1
        while(left<right):
            mid=(left+right)//2
            if arr[mid]>arr[right]:
                left=mid+1
            else:
                right=mid
        return arr[left]