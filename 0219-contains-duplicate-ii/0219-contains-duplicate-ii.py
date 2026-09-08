class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window=set()
        n=len(nums)
        for i in range(n):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window)>k:
                window.remove(nums[i-k])
        return False