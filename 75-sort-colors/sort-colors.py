class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)-1):
            min_ele=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[min_ele]:
                    min_ele=j
            nums[i],nums[min_ele]=nums[min_ele],nums[i]
        return nums