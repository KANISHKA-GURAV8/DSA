class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_len=float('inf')
        sum=0
        i=0
        for j in range(0,len(nums)):
            sum=sum+nums[j]
            while sum>=target:
                min_len=min(min_len,j-i+1)
                sum=sum-nums[i]
                i+=1
        return 0 if min_len==float('inf') else min_len
        


        