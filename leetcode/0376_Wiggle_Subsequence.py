# A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. 
# The first difference (if one exists) may be either positive or negative. 
# A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.
# A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

# Given an integer array nums, return the length of the longest wiggle subsequence of nums.

 
# Greedy approach, using flag. When we find a valid wiggle, we continue. Note that if it is not a valid wiggle, we can just disregard the previous (as the chance for wiggle is higher). 
    # Time Complexity: O(N)
    # Space Complexity: O(1)
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # If the string is 1 or 0 length, it is already a valid wiggle. 2 could possibly not wiggle (eg. [0, 0])
        if len(nums) < 2:
            return len(nums)
        
        max_length = 1
        # Variable will tell us if the next number should go upwards. 
        up_next = None
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] and up_next != False: # Condition has to be like this, in order to get past the initialisation at None. 
                max_length += 1
                up_next = False
            
            elif nums[i] < nums[i - 1] and up_next != True:
                max_length += 1
                up_next = True            
            
        return max_length
            