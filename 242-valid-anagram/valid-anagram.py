class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_freq={}
        t_freq={}
        for i in range(0,len(s)):
            if s[i] in s_freq:
                s_freq[s[i]]+=1
            else:
                s_freq[s[i]]=1
        
        for j in range(0,len(t)):
            if t[j] in t_freq:
                t_freq[t[j]]+=1
            else:
                t_freq[t[j]]=1
        
        if s_freq==t_freq:
            return True
        else:
            return False

        