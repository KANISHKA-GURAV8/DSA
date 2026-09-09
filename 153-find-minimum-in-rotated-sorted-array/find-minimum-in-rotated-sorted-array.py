class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=len(nums)-1
        min_el=float('inf')
        while i<=j:
            mid=(i+j)//2
            if nums[i]==nums[mid]==nums[j]:
                min_el=min(min_el,nums[mid])
                i+=1
                j-=1
            elif nums[i]<=nums[mid]:
                min_el=min(min_el,nums[i])
                i=mid+1
            else:
                min_el=min(min_el,nums[mid])
                j=mid-1
        return min_el


        