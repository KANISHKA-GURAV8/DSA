class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        hash_map={}
        i=0
        max_len=0
        for j in range(len(fruits)):
            if fruits[j] in hash_map:
                hash_map[fruits[j]]+=1
            else:
                hash_map[fruits[j]]=1

            while len(hash_map)>2:
                hash_map[fruits[i]]-=1
                if hash_map[fruits[i]]==0:
                    del hash_map[fruits[i]]
                i+=1

            max_len=max(max_len,j-i+1)
        return max_len

            
