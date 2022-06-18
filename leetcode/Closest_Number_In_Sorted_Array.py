# Given a target number and an integer array A sorted in ascending order, find an index i in A such that A[i] is closest to the given target.
# Return -1 if there is no element in the array.


# Binary search to find the first number that is larger than the target.
    # We can compare this number to the previous indexed one, and return the index of the closer number. 
    # Time Complexity: O(logn)
    # Space Complexity: O(1)
class Solution:
    def closest_number(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        # If no array
        if not nums: 
            return -1
        
        # Check if number is smaller than all numbers
        if nums[0] >= target:
            return 0
        
        # Check if number is larger than all numbers
        if nums[-1] <= target:
            return high

        # Binary search to find the first number bigger than the target. Checks above guarantee that this will exist and be larger than the 0th index and smaller than our highest number. 
        # Loop exits when low and high and mid are on the same number (first largest)
        while low < high:
            mid = low + (high - low)//2
            val = nums[mid]

            if val == target:
                return mid
            
            elif val < target:
                low = mid + 1
            
            else:
                high = mid

        # Compare closest largest to closest smallest
        if nums[low] - target < target - nums[low - 1]:
            return low
        
        else:
            return low - 1