class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_map={}
        for sen in strs:
            sort_s="".join(sorted(sen))
            if sort_s in hash_map:
                hash_map[sort_s].append(sen)
            else:
                hash_map[sort_s]=[sen]
        
        return list(hash_map.values())

        




