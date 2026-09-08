class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix=0
        n=len(nums)
        if sum(nums[1:])==0:
            return 0
        for i in range(1,n):
            prefix+=nums[i-1]
            right=sum(nums[i+1:])
            if prefix==right:
                return i
        return -1
        