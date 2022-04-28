# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

# METHOD 1: TWO POINTERS. Two pointers are initiated at each end of the array. We check to see if the indexed number is out of position by checking it against the next one.
# Once we find the first instances of unsorted numbers, we form a subarray between them (inclusively) and find minimums and maximums inside the subarray.
# When we have the minimums and maximums, we know how far we have to expand the subarray: to the first smaller number on the right side, and to the first larger number on the left side. 
## Remember, we can stop at the first one because these outer numbers are in sorted order. 
# This implementation makes sure that left and right pointers DO NOT cross (only situation they cross is if the array is already sorted, and we have an escape condition for this)
# Time complexity: O(N) // Space complexity: O(1)
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # We place pointers on the left and right and check if the array is correct up and down
        left = 0
        right = len(nums) - 1

        # For left indexes, we check if number is valid by checking if it is SMALLER than the number IN FRONT. If it is not valid, then the index is the start of our unsorted subarray
        while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
            left += 1

        if left == len(nums) - 1:  # Checks if the array is sorted (no need to do it again with the right index, because the conditions are the same)
            return 0

        # For right indexes, we check if number is valid by seeing if it is LARGER than the number to the left. If not, then this is the end of our sorted subarray
        while (right > 0 and nums[right] >= nums[right - 1]):
            right -= 1
            
        
        # Find the maximum and minimum numbers in the subarray by iterating through the array and storing a max and min
        sub_max = -inf
        sub_min = inf
    
        for i in range(left, right + 1):
            sub_max = max(nums[i], sub_max)
            sub_min = min(nums[i], sub_min)

        # Expand the edges of the subarray, checking for the first non-sorted outer number
        while left > 0 and nums[left - 1] > sub_min:
            left -= 1
        
        while right < len(nums) - 1 and nums[right + 1] < sub_max:
            right += 1
        
        return right - left + 1
        
    ## ALTERNATE IMPLEMENTATION OF THE EXPANSION - FROM THE ENDS TO THE MIDDLE
        # Left and right expansion pointers, modifying the array. 
        # Stopping at the first of many duplicates is NOT an issue (despite trying to achieve the smallest subarray), as ALL invalid duplicates will have to be sorted. 
        # l = 0
        # r = len(nums) - 1
        
        # while nums[l] <= sub_min:
            # l += 1
        
        # while nums[r] >= sub_max:
            # r -= 1
        # return r - l + 1
    


# METHOD 2: Sorting (easier, less efficient solution)
# Sort the array first. Then compare the values at each index with two pointers, starting from the left and right. 
# The first indices that do not match values are the indices of the subarray that needs to be sorted. 
# Time complexity: O(nlogn) for sorting // Space complexity: O(N) as we have to duplicate the original array

def findUnsortedSubarray(self, nums: List[int]) -> int:
    # Sort array and find indices of places
    sorted = nums.copy()
    sorted.sort()
    
    # Initiate pointers. Then find the indices at the first instances where the pointers do not match
    l = 0
    r = len(nums) - 1
    
    for l in range(len(nums)): 
        if nums[l] != sorted[l]:
            break

    for r in range(len(nums) - 1, 0, -1): 
        if nums[r] != sorted[r]:
            break
    
    # If the pointers cross over, this means that there was no difference. HAS TO INCLUDE THE EQUALS to account for the edge cases where there is only one element in the index. 
    if l >= r: 
        return 0
    
    # Length of the subarray is returned
    return (r - l + 1)
