class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        first_element=0
        for i in range(0,len(nums)):
            if nums[i]%2==0:
                nums[first_element],nums[i]=nums[i],nums[first_element]
                first_element+=1
        return nums