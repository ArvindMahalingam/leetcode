class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        match1={}
        match2={}
        for chars,chart in zip(s,t):
            if chars in match1:
                if match1[chars] !=chart:
                    return False
            else:
                match1[chars]=chart
            
            if chart in match2:
                if match2[chart] !=chars:
                    return False
            else:
                    match2[chart]=chars
        return True
        
        