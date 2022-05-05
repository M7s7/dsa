# Given an unsorted integer array nums, return the smallest missing positive integer.
# You must implement an algorithm that runs in O(n) time and uses constant extra space.



# METHOD 1: CYCLIC SORT
    # We should be trying to get our array to like this:
    # INDEX: 0 1 2 3 4 ...(N-1)
    # VALUE: 1 2 3 4 5 ... N
# Thus, all the numbers in the array will be placed on the right indices.  # We will return the first 1-indexed index that is not sorted. 
    # Time complexity: O(N) // Space complexity: O(1)

def firstMissingPositive(self, nums):
        i = 0
        n = len(nums)
        # Lets go through the array
        while i < n:
            # The number should be on the index (value - 1)
            j = nums[i] - 1
            
            # If number is on wrong index AND number is positive AND number is in range (not over N), we will swap
            if i != j:
                if nums[i] >= 1 and nums[i] <= n and nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                # If duplicate number in wrong index, just iterate over it
                else: i += 1 
            # Number is in the right position
            else:
                i += 1
        
        # Now that the array is sorted, we will find the first index with the incorrect number in it. Return the number that should be there
        for i, value in enumerate(nums):
            if i != value - 1:
                return (i + 1)
            
        # Else, if there is no missing number, we will return the NEXT number (N + 1)
        return n + 1


# NEGATIVE MARKING TBD