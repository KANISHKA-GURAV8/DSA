class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map={}
        for i in range(0,len(nums)+1):
            if i in nums:
                hash_map[i]=1
            else:
                return i

        
        