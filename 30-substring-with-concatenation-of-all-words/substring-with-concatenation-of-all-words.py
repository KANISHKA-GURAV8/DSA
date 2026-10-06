class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len=len(words[0])
        hash_map={}
        substring="".join(words)
        len_substrings=len(substring)
        result=[]
        for word in words:
            if word in hash_map:
                hash_map[word]+=1
            else:
                hash_map[word]=1
        
        for i in range(len(s) - len_substrings + 1):
            candidate= s[i:i+len_substrings] 
            chunks = [candidate[j:j+word_len] for j in range(0, len_substrings, word_len)]
            temp_map={}
            for word in chunks:
                if word in temp_map:
                    temp_map[word]+=1
                else:
                    temp_map[word]=1

            if temp_map==hash_map:
                result.append(i)
        return result




        
        