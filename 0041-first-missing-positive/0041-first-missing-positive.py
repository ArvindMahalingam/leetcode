class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited=set(nums)
        smallest=1
        while smallest in visited:
            smallest=smallest+1
        return smallest
        
        