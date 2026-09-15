class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        def robber(nums):
            n=len(nums)
            dp=[-1]*(n)
            dp[0]=nums[0]
            if len(nums)==1:
                return nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(2,n):
                dp[i]=max(nums[i]+dp[i-2],dp[i-1])
            return max(dp[n-1],dp[n-2])
        
        n=len(nums)
        return max(robber(nums[1:]),robber(nums[:-1]))
        

        