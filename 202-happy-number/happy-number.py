class Solution:
    def isHappy(self, n: int) -> bool:
        hash_map={}
        def ishappy(n):
            sum=0
            while n!=0:
                num=n%10
                sum=sum+(num**2)
                n//=10
                
            if sum==1:
                return True
            
            if sum not in hash_map:
                hash_map[sum]=True
                return ishappy(sum)
            else:
                return False
        return ishappy(n)
                
           
        




    
        


        




        
        