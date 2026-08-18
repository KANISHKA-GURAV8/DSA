class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hash_map = {}
        i = 0
        max_len = 0

        for j in range(len(s)):
            if s[j] in hash_map and hash_map[s[j]] >= i:
                # move left pointer past the last occurrence
                i = hash_map[s[j]] + 1

            # update last seen index
            hash_map[s[j]] = j

            # update max length
            max_len = max(max_len, j - i + 1)

        return max_len


        


        