class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hash_map={}
        for j in range(0,len(nums)):
            if nums[j] in hash_map and j-hash_map[nums[j]]<=k:
                return True
            hash_map[nums[j]]=j
        return False



                
            
        