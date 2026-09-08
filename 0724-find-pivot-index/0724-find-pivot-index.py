class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix=0
        total=sum(nums)
        for i in range(len(nums)):
            right=total-nums[i]-prefix

            if right==prefix:
                return i
            prefix+=nums[i]
        return -1        