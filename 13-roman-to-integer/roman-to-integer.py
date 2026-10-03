class Solution:
    def romanToInt(self, s: str) -> int:
        hash_dict={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        # count=0
        # for i in range(0,len(s)-1):
        #     if str(s[i]+s[i+1]) in hash_dict or s[i] in hash_dict:
        #         count+=hash_dict[s[i]]
        #     else:
        #         count=count+(s[i]-s[i+1])
        # return count
        count=0
        i=0
        while i<len(s):
            if i+1<len(s) and s[i]+s[i+1] in hash_dict:
                count+=hash_dict[s[i]+s[i+1]]
                i+=2
            else:
                count+=hash_dict[s[i]]
                i+=1
        return count

                



        
