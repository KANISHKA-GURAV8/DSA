class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash_map={}
        for i in range(0,len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]]+=1
            else:
                hash_map[nums[i]]=1

        sorted_by_values = sorted(hash_map.items(), key=lambda x: x[1],reverse=True)

        result=[]
        for key,value in sorted_by_values[:k]:
            result.append(key)
        return result