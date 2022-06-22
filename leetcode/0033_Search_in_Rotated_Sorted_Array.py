# There is an integer array nums sorted in ascending order (with distinct values). nums is possibly rotated at a point.
# Return the index of the target; if not in the index, return -1. 

# Approach: Binary search. Binary search only works if the array is sorted. 
    # Since at least either the left or right will be sorted (only one pivot point), we can use this array (either by confirmation or ommission) to check which side the target is on. 
    # We have to be very explicit with our checking function (using two sided inequality) - otherwise, we will run into MANY various edge case errors, including the ones below. 
        # Time Complexity: O(logN) for binary search
        # Space Complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + (high - low)//2
            # Check if mid is target
            if nums[mid] == target:
                return mid
            
            # If right is non-rotated, it is sorted so we can search for the target
            if nums[mid] < nums[high]:
                # If the target is in the right, we keep it
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1          
                # If not, we can infer that it the target is in the left 
                else:
                    high = mid - 1
             
            # Else, if left is non-rotated, we can search for target
            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1    
                else:
                    low = mid + 1
        # If target is not found
        return -1

# Edgecases
# 1) [4,5,6,7,0,1,2] target = 0.
    # Mid is on the rotation point. If we do not include the double inequality (and instead opt for a single inequality like target <= nums[mid]), we will not find the target. 
    # Runthrough: The left will be considered as sorted. Since the target is smaller than mid, we will shrink to the left side. This will immediately be wrong as we have deleted the target from our search space. 
    
    # The way we fix this is to be more explicit with our target finding by placing a double sided inequality.
# 2) [1,3] target = 3.
    # If we do not check for <= in our double sided inequality, we will return the wrong number.
    # Thus, although we always check mid for the target, we still need to use <= in the bounds checking. 