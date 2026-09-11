class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n=len(nums)
        best_sum=nums[0]
        current_sum=nums[0]
        current_min=nums[0]
        worst_sum=nums[0]
        total=sum(nums)
        for i in range(1,n):
            current_sum=max(nums[i],nums[i]+current_sum)
            best_sum=max(best_sum,current_sum)
            current_min=min(nums[i],nums[i]+current_min)
            worst_sum=min(worst_sum,current_min)
            
        circular_sum=total-worst_sum
        if best_sum<0:
            return best_sum
        return max(best_sum,circular_sum)

        