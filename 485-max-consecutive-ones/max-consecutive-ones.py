class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        max_num=0
        count=0
        for j in range(len(nums)):
            if nums[j]==1:
                count+=1
            else:
                count=0
            max_num=max(max_num,count)
        return max_num

            