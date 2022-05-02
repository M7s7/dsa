# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.

# Both solutions below are using partitioning with TWO POINTERS, sorting in-place.
# Time complexity: O(N) // Space complexity: O(1)

def sortArrayByParity(self, nums):
    # Initialise pointers
    start = 0
    
    for i, value in enumerate(nums):
        # If number is even, move it to the start
        if value % 2 == 0:
            nums[i], nums[start] = nums[start], nums[i]
            # Increment the start value
            start += 1
    return nums



# If we want to avoid unnecessary swaps:

def sortArrayByParity(self, nums: List[int]) -> List[int]:
    # Initialise pointers
    start = 0
    
    for i, value in enumerate(nums):
        # If number is even, move it to the start
        if value % 2 == 0:
            if nums[start] % 2 != 0: # THIS IS THE ADDED LINE, actually might make it slower due to checking the condition every time
                nums[i], nums[start] = nums[start], nums[i]
            # Increment the start value
            start += 1
    return nums