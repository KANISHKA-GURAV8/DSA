class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        st=0 
        end=len(nums)-1
        self.merge_sort(nums,st,end)
        return nums

    def merge_sort(self,nums,st,end):
        if st<end:
            mid=(st+end)//2
            self.merge_sort(nums,st,mid)
            self.merge_sort(nums,mid+1,end)
            self.mergesort(nums,st,mid,end)

    def mergesort(self,nums,st,mid,end):
        left=[]
        for i in range(st,mid+1):
            left.append(nums[i])

        right=[]
        for i in range(mid+1,end+1):
            right.append(nums[i])

        i=0
        j=0
        k=st
        while i<len(left) and j<len(right):
            if left[i]>right[j]:
                nums[k]=right[j]
                j+=1
            else:
                nums[k]=left[i]
                i+=1
            k+=1

        while i<len(left):
            nums[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            nums[k]=right[j]
            j+=1
            k+=1

                            






        
        