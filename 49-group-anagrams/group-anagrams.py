class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash_map={}
        for word in strs:
            sorted_w="".join(sorted(word))
            if sorted_w in hash_map:
                hash_map[sorted_w].append(word)
            else:
                hash_map[sorted_w]=[word]

        result=[]
        for k,v in hash_map.items():
            result.append(v)
        return result
                    