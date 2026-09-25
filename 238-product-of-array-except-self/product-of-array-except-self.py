class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # result=[]
        # for i in range(0,len(nums)):
        #     product=1
        #     for j in range(0,len(nums)):
        #         if i==j:
        #             continue
        #         else:
        #             product=product*nums[j]
        #     result.append(product)
        # return result
        n=len(nums)
        left_prefix=[]
        prefix=1
        for i in range(0,len(nums)):
            left_prefix.append(prefix)
            prefix*=nums[i]

        right_prefix=[0]*n
        prefix=1
        for i in range(len(nums)-1,-1,-1):
            right_prefix[i]=prefix
            prefix*=nums[i]

        result=[]
        for i , j in zip(left_prefix,right_prefix):
            result.append(i*j)
        return result


        