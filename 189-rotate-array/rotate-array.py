class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=0
        k=k%n
        def reverse_func(i,j):
            while i<=j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1

        reverse_func(0,n-1)
        reverse_func(0,k-1)
        reverse_func(k,n-1)
        


        