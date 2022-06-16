# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].


# Modified Binary Search - Two calls - one for upper bound, one for lower
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find lower bound
        low, high = 0, len(nums) - 1
        
        # Loop exits when low and high are the same.
        while low <= high:
            # Mid is biased to the left to avoid an infinite loop
            mid = low + (high - low)//2
            mid_val = nums[mid]
            # Low bound moves and excludes mid if condition is met
            if mid_val < target:
                low = mid
            
            else:
                high = mid
        
        # Check if the number is actually in the array. Checking if nums exists for empty array edge case
        if nums and nums[low] == target:
            floor = low
       
        # If floor doesn't exist, then the number doesn't exist. Return invalid
        else:
            return [-1, -1]
        
        # Find upper bound
        low, high = 0, len(nums) - 1
        
        while low <= high:
            # Mid is right-biased to avoid infinite loop
            mid = low + (high - low + 1)//2
            mid_val = nums[mid]
            
            if mid_val > target:
                high = mid
                
            else:
                low = mid
        
        ceiling = low
        return [floor, ceiling]
        


# Modified Binary Search - using functions to reduce code. Slightly different implementation
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = self.binarySearch(nums, target, True)
        high = self.binarySearch(nums, target, False)
        
        return [low, high]
        
    def binarySearch(self, nums, target, lower: bool):
        low, high = 0, len(nums) - 1
        # Initialise bound as invalid. If we don't find the number, bound will return invalid
        bound = -1
        
        # Since we are trying to find a specific number, we use <= instead of <
        while low <= high:
            mid = low + (high - low)//2
            mid_val = nums[mid]

            if mid_val < target:
                low = mid + 1

            elif mid_val > target: 
                high = mid - 1

            # If we have the target number on mid, we want to find the bounds by continuing our search
            else:
                bound = mid
                # Although mid = target, we don't know if we have our bounds, so shrink our search space
                if lower:
                    high = mid - 1 # Finding lower bound means that we shift the high pointer to exclude mid
                else:
                    low = mid + 1 # Finding upper bound means that we shift the low pointer to exclude mid

        return bound