# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Cyclic sort. Sort as many numbers as we can to the right indices, skipping duplicate swaps because they indicate a missing number. 
# After the sort, sweep through the nums list and find the numbers which are not in the right indices
# Time complexity: O(N), 2N as we pass through array twice // Space complexity: O(1) if we don't count the return list

def findDisappearedNumbers(self, nums):
    # Initiate variables - i is start of nums list, missingno returns missing numbers
    i = 0
    missingNo = []
    
    # All numbers in our expected range CAN fit in the array. We will CYCLIC sort the numbers, placing as many numbers in sorted order ([1, 2, 3, 4, ..., n])
    while i < len(nums):
        # All numbers should have an index of -1 of its value. We will call this number j
        j = nums[i] - 1
        
        # If the number is in the wrong spot and we are not swapping to a duplicate number, we swap the number nums[i] to the correct index
        if i != j and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

                
        # If the number is in the right spot or if we have encountered a duplicate swap, we want to skip to the next index
        else: i += 1
    
    # Pass through the array again to find any numbers out of order (ie. index is not value - 1). We find the indices where the missing numbers should be; we can return the appropriate values (eg. i + 1)
    for i, value in enumerate(nums):
        if i + 1 != value:
            missingNo.append(i + 1)
    
    return missingNo


# MARKING INDICES. We can mark indices as negative if a number should exist there. Then we can go through the array and return the numbers that should be on the positive valued indices.
# Time complexity: O(N) // Space complexity: O(1)

def findDisappearedNumbers(self, nums):
    missingNo = []        

    for value in nums:
        # Appropriate index for the value is (value - 1)
        i = abs(value) - 1
        # Mark the number on that index as negative. We need to take the absolute value because it may already be marked negative.
        nums[i] = -1 * abs(nums[i])
        
    # If nums[i] is positive, it indicates that the number that was meant to be on index i is missing. 
    for i, value in enumerate(nums):
        if value > 0: 
            missingNo.append(i + 1)

    return missingNo