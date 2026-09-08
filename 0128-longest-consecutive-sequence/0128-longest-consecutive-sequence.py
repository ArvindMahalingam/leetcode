class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        array=set(nums)
        max_length=0
        
        for x in array:
            if x-1 not in array:
                length=1
                while(x+length in array):
                    length+=1
                        
                max_length=max(max_length,length) 
        return max_length
        