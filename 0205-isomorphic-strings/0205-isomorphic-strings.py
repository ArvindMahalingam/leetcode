class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
   return False
        match1={}
        match2={}
        for       :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        n=len(s)
        mp1={}
        mp2={}
        for i in range(n):
            if s[i] in mp1:
                if mp1[s[i]] != t[i]:
                    return False
            else:
                mp1[s[i]]=t[i]
            
            if t[i] in mp2:
                if mp2[t[i]] != s[i]:
                    return False
            else:
                mp2[t[i]]=s[i]
        return True
        
        