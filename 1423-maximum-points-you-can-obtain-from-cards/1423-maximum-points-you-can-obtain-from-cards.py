class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n=len(cardPoints)
        value=n-k
        window_sum=sum(cardPoints[:value])
        minimum=window_sum
        for i in range(value,n):
            window_sum-=cardPoints[i-value]
            window_sum+=cardPoints[i]
            minimum=min(minimum,window_sum)
        return sum(cardPoints)-minimum
        