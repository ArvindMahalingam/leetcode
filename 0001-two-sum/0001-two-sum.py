class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        n=len(nums)
        for i in range(n):
            need=target-nums[i]
            if need in hashmap:
                return [hashmap[need],i]
            hashmap[nums[i]]=i
        