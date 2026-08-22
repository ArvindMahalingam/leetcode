class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words=s.split()
        if len(pattern) != len(words):
            return False
        match1={}
        match2={}
        for charp,word in zip(pattern,words):
            if charp in match1:
                if match1[charp] !=word:
                    return False
            else:
                match1[charp]=word
            if word in match2:
                if match2[word] !=charp:
                    return False
            else:
                match2[word]=charp
        return True
        