class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i=0
        for j in range(0,len(nums)):
            if nums[j]==val:
                continue
            else:
                nums[i]=nums[j]
                i+=1
        return i