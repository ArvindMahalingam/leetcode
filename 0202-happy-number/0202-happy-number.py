class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited=set()
        
        while n!=1:
            value=0
            visited.add(n)
            for i in str(n):
                value+=int(i)**2
            n=value
            if value in visited:
                return False

        return True

        