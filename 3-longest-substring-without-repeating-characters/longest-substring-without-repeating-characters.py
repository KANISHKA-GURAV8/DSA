class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map={}
        i=0
        max_len=0
        for j in range(len(s)):
            if s[j] in hash_map and hash_map[s[j]]>=i:
                i=hash_map[s[j]]+1
            hash_map[s[j]]=j
            max_len=max(max_len,j-i+1)
        return max_len