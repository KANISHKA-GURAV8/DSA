class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash_fre={0:1}
        prefix_sum=0
        count=0
        for num in nums:
            prefix_sum+=num
            if (prefix_sum-k) in hash_fre:
                count+=hash_fre[prefix_sum-k]

            if prefix_sum in hash_fre:
                hash_fre[prefix_sum]+=1
            else:
                hash_fre[prefix_sum]=1
        return count
        


        