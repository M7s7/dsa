# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
# Return k after placing the final result in the first k slots of nums.
# There is a more efficient solution, using swapping 
# Time complexity: O(N). Space complexity: O(1)

def removeElement(self, nums: List[int], val: int) -> int:
    # Only need one pointer - the 'index' pointer to iterate over the array can be replaced with actually iterating over the list itself
    location = 0
    # Iterate over the array and search for non-val numbers
    for num in nums:
        # If non-val element found, place it in the 'new' array
        if num != val: 
            nums[location] = num
            # Move location pointer, getting it ready for the next non-val integer
            location += 1
    # Location is an index that is zero-indexed. However, we don't need to add 1 to get length because next automatically shifts up one after insertion
    return location
        