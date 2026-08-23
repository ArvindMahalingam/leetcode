class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def questionmark(num):
            count=0
            for i in num:
                if i=="?":
                    count+=1
            return count
        total_count=questionmark(num)
        if total_count%2==1:
            return True
        
        n=len(num)
        left_count=questionmark(num[:n//2])
        right_count=questionmark(num[n//2:])
        left_sum=0
        right_sum=0
        for i in num[:n//2]:
            if i != "?":
                left_sum+=int(i)
        for i in num[n//2:]:
            if i !="?":
                right_sum+=int(i)
        return (left_sum - right_sum) != (right_count - left_count) // 2 * 9

        
        


        