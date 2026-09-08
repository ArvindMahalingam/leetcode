class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        map1={}
        for i in ransomNote:
            if i in map1:
                map1[i]+=1
            else:
                map1[i]=1
        map2={}
        for i in magazine:
            if i in map2:
                map2[i]+=1
            else:
                map2[i]=1
        
        for i in map1:
            if i not in map2:
                return False
            if( map1[i]>map2[i]):
                return False
            
        return True
        