# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. 

# This solution uses Kadane's algorithm. We disregard previous negative subarrays.  
# Time: O(N) // Space: O(1)

import math

class Solution:
    def maxSubArray(self, nums) -> int:
        currSum = 0
        maxSum = -math.inf # Edgecase - if the array only contains negative subarrays, we don't want to return 0
        
        for val in nums:
            # Discard previous current sum if negative, returning it to zero
            if currSum < 0:
                currSum = 0
            
            # Add new element to current sum
            currSum += val

            # Return max
            maxSum = max(currSum, maxSum)
        return maxSum