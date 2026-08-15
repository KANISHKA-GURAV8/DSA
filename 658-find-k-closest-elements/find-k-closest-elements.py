from bisect import bisect_left
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # Step 1: Find insertion point for x
        pos = bisect_left(arr, x)
        
        # Step 2: Initialize two pointers
        left, right = pos - 1, pos
        
        # Step 3: Expand window until we have k elements
        while right - left - 1 < k:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        # Step 4: Return the slice (already sorted)
        return arr[left + 1:right]
