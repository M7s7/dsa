# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.

# Initialise a window and extend it until it is greater or equal to total. Store the min_length.
# Shrink the window from the left as much as we can. Every time we reduce and it is still valid, store that value
# Time complexity: O(N) // Space complexity: O(1)
from math import inf

def minSubArrayLen(self, target, nums):
    # Initiate our window pointer start, windowSum and placeholder for min length
    start = 0
    windowSum = 0
    min_length = inf
    
    for end, value in enumerate(nums):
        # Add the value to the windowSum
        windowSum += value
        
        # Conditional if windowSum is valid
        while windowSum >= target:
            # Store the value of the windowSum
            min_length = min(min_length, end - start + 1)
            # Remove digits from the start of the window, checking if the window is still valid
            windowSum -= nums[start]
            start += 1
    
    # If there is no valid answer, we will return 0
    if min_length == inf:
        return 0
    
    return min_length