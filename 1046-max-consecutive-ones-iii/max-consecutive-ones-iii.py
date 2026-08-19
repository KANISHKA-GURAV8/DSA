class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 0   # left pointer
        max_len = 0
        count = 0  # number of zeros in window

        for j in range(len(nums)):
            if nums[j] == 0:
                count += 1
                
            while count > k:
                if nums[i] == 0:
                    count -= 1
                i += 1

            max_len = max(max_len, j - i + 1)

        return max_len

        