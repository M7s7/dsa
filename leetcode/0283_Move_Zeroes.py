# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Two pointer question. Partition the left side by swapping non-zero numbers to it. 
# Time complexity: O(N) // Space complexity: O(1)
def moveZeroes(self, nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    # Create two pointers - one pointer initialised at the start, and another pointer iterating through the array finding non-zero digits
    start = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            # If we find a non-zero number, swap it with the starting value
            nums[i], nums[start] = nums[start], nums[i]
            # Increment start
            start += 1