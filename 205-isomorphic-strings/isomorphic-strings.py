class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_s={}
        hash_t={}
        for i,j in zip(s,t):
            if i in hash_s and hash_s[i]!=j:
                return False
            else:
                hash_s[i]=j

            if j in hash_t and hash_t[j]!=i:
                return False
            else:
                hash_t[j]=i
        return True