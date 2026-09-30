class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map1={}
        hash_map2={}
        for char in ransomNote:
            if char in hash_map1:
                hash_map1[char]+=1
            else:
                hash_map1[char]=1

        for char in magazine:
            if char in hash_map2:
                hash_map2[char]+=1
            else:
                hash_map2[char]=1

        for k,v in hash_map1.items():
            if v > hash_map2.get(k,0):
                return False
        return True


        
        