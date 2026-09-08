class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited=set()

        
        while (n != 1):
            square=0
            visited.add(n)
            for i in str(n):
                square+=int(i)**2
            n=square
            if n in visited:
                return False
        return True
            

        