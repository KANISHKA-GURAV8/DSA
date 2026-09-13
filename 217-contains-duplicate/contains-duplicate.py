class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq_num={}
        for i in range(0,len(nums)):
            if nums[i] not in freq_num:
                freq_num[nums[i]]=1
            else:
                freq_num[nums[i]]+=1
        
        for k,v in freq_num.items():
            if v>=2:
                return True
        return False
        