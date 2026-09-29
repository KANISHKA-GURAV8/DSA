class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        count=1
        for j in range(1,len(nums)):
            if nums[i]==nums[j]:
                count+=1
                if count <= 2:
                    i+=1
                    nums[i]=nums[j]
            else:
                count=1
                i+=1
                nums[i]=nums[j]
        return i+1
                
                
            


