class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        best_sum=nums[0]
        current_sum=nums[0]

        for i in range(1,n):
            current_sum=max(nums[i],nums[i]+current_sum)
            best_sum=max(best_sum,current_sum)
        return best_sum        
            
