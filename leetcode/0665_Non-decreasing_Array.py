# Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
# We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

# TWO POINTERS: Check the elements in pairs. If the right element is smaller than the left element, then we have an error and we must change an element. 
# Ideally, we would like to change the numbers to the SMALLER of the two (as this will still make it 'increasing'). However, if this modifies the LEFT element, then the left-left element might be bigger still. eg. [3, [4, 1]] - changing to 1 would be invalid
# Thus, we have to check if this modification will still be valid in relation to the element directly LEFT of the pairs to choose whether we go with a large or small modification. 
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    # Note that the solution will modify our input.

    # Approach 1: My implementation. Our i is the RIGHT element of the pair.
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = True
        
        # Starts at index 1. 
        for i in range(1, len(nums)):
            # Condition: The array is no longer increasing. 
            if nums[i - 1] > nums[i]:
                # If we go through this condition twice, then we will have violated the conditions. We return False
                if flag == False:
                    return flag
                flag = False

                # Check if we swap to the smaller number or not. 
                if i > 1 and nums[i] < nums[i - 2]: # Remember, we know that num[i - 1] is LARGER, and num[i] is smaller
                    nums[i] = nums[i - 1]
                   
                else:
                    nums[i - 1] = nums[i]
        return True
                
    
    # Approach 2: Forward-looking. Our element is the LEFT element of the pair.  
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flag = True

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if flag == False:
                    return flag
                flag = False

                if i > 0 and nums[i + 1] < nums[i - 1]:
                    nums[i + 1] = nums[i]

                else:
                    nums[i] = nums[i + 1]
        return True
                
                