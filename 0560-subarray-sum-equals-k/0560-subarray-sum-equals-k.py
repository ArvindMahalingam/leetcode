class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix=0
        count=0
        mp={0:1}
        for i in nums:
            prefix=prefix+i
            need=prefix-k
            if need in mp:
                count+=mp[need]
            mp[prefix]=mp.get(prefix,0)+1
        return count
       
        