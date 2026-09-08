class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        prefix=0
        mp={0:-1}
        ans=0
        for i in range(n):
            if nums[i]==0:
                prefix=prefix-1
            else:
                prefix+=1
            
            if prefix in mp:
                ans=max(ans,i-mp[prefix])
            else:
                mp[prefix]=i
        return ans




        