class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq={}
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1

        items=list(freq.items())
        for i in range(0,len(items)):
            max_ele=i
            for j in range(i+1,len(items)):
                if items[j][1]>items[max_ele][1]:
                    max_ele=j
            items[i],items[max_ele]=items[max_ele],items[i]
        
        result=""
        for char,count in items:
            result+=char*count
        return result
