class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s={}
        for i in range(len(s)):
            if s[i] in hash_s:
                hash_s[s[i]]+=1
            else:
                hash_s[s[i]]=1

        hash_t={}
        for i in range(len(t)):
            if t[i] in hash_t:
                hash_t[t[i]]+=1
            else:
                hash_t[t[i]]=1

        if hash_s==hash_t:
            return True
        else:
            return False
