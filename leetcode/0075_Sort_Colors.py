# Sort an array in place. The array may have a mix of 0s, 1s and 2s.
# You must solve this problem without using the library's sort function.
# Initialise three pointers - left stores 0s, right stores 2s and index scans the array. 
# Time complexity is O(N) // Space complexity is O(1)

def sortColors(self, nums: List[int]) -> None:
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
