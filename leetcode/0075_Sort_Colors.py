# Sort an array in place. The array may have a mix of 0s, 1s and 2s.
# You must solve this problem without using the library's sort function.


# METHOD 1: Optimal Two Pointer solution
# Initialise three pointers - left stores 0s, right stores 2s and index scans the array. 
# Time complexity is O(N) // Space complexity is O(1)

def sortColors(self, nums):
    # Initialise pointers. Store zeroes on the left, twos on the right. Index passes through the array.
    left = 0 
    right = len(nums) - 1
    i = 0
    
    # Create while loop, with condition (as everything the the right of right pointer is already sorted)
    while i <= right:
        # If index is zero, we want to swap it with the left pointer
        if nums[i] == 0:
            nums[left], nums[i] = nums[i], nums[left]
            # Increment to next position to hold next zero
            left += 1
        
        # If index is two, we want to swap with right pointer
        if nums[i] == 2:
            nums[right], nums[i] = nums[i], nums[right]
            # Decrement to next position to hold next two
            right -= 1
            # Since index has been swapped with an unknown number that was on the right pointer, we have to check it again. We can do this by stalling index
            i -= 1
        i+= 1


# OPTION 2: BUCKETSORT - store frequency of values and then rebuild the array from the start
# Quite messy, but it is still Time Complexity of O(N) (albeit with a larger constant, seems like its 4N) // Space complexity is O(1) (as we always only store 3 values in the hashmap)
def sortColors(self, nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    # Bucketsort solution
    freq = {0: 0, 1: 0, 2: 0}
    
    for value in nums:
            freq[value] += 1
            
    # Change in-place
    index = 0
    
    print(freq)
    while freq[0] > 0:
        nums[index] = 0
        index += 1
        freq[0] -= 1
        
    while freq[1] > 0:
        nums[index] = 1
        index += 1
        freq[1] -= 1   
        
    while freq[2] > 0: 
        nums[index] = 2
        index += 1
        freq[2] -= 1
    return