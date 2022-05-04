
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant extra space.


# METHOD 1: CYCLIC SORT. 
    # Since the range is from 1 to n, non duplicated nums array would have each number, where the number = index + 1. Thus, we can sort the numbers like this and check for numbers out of place. We can return these numbers.
        # INDEX: 0 1 2 3 4 5 6
        # NUMBER:1 2 3 4 5 6 7
    # Time Complexity: O(N) (n+n due to two passes) // Space Compexity: O(1)

def findDuplicates(self, nums):
    dupes = []
    i = 0
    
    # Sort in place through cyclic sort
    while i < len(nums):
        # As said above, a number is in the right place if its index is value - 1. 
        j = nums[i] - 1
        
        # If the number is in the wrong spot and is not swapping with a duplicate, we can swap them
        if j != i and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            continue
        
        # If the number is a duplicate or is in the right spot, go to the next index
        i += 1
    
    # Pass over the array again and check to see which numbers are out of their place - remember, if the number's value - 1 is not its index, it is out of place. 
    for index, value in enumerate(nums):
        if value - 1 != index:
            dupes.append(value)
    return dupes


# METHOD 2: HASHING VALUES BY NEGATIVE MARKING
    # We can use the array itself to mark numbers that we have visited. For each number x, we will visit nums[x] and flip its value. Then, we will go through the array and return the positive indices.
    # This method only works because a number can only appear a maximum of TWICE. Thus, when we visit an index and its already negative, we know that the (index + 1) value is a duplicate number. 
# Time Complexity: O(N) // Space complexity: O(1)

def findDuplicates(self, nums):
    dupes = []
    
    for i, value in enumerate(nums):
        # We must take the absolute value when determining the index this number belongs to as the value might be marked negative
        j = abs(value) - 1
        
        # Mark numbers as negative - if number was already negative, it was duplicated. Remember that the value of the duplicate would be the INDEX + 1
        if nums[j] < 0:
            # Now that we know which index is a duplicate number corresponds to, we should un-zero index it and add it to answers
            number = j + 1
            dupes.append(number)
        
        # If number has not been marked yet, we should mark it
        else: nums[j] *= -1
    return dupes