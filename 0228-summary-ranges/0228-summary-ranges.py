class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        results=[]
        i=0

        while (i<len(nums)):
            start=nums[i]

            while(i<len(nums)-1 and nums[i]+1==nums[i+1]):
                i+=1

            if start!=nums[i]:
                results.append(str(start)+"->"+str(nums[i]))
            else:
                results.append(str(start))
            i+=1

        return results

        
            


        