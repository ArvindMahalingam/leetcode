class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        map1={}
        map2={}
        words=s.split()
        if len(pattern) != len(words):
            return False
        
        n=len(words)
        for i in range(n):
            if pattern[i] in map1:
                if map1[pattern[i]] !=words[i]:
                    return False
            else:
                    map1[pattern[i]]=words[i]
            
            if words[i] in map2:
                if map2[words[i]] != pattern[i]:
                    return False
            else:
                    map2[words[i]]=pattern[i]
        return True
        