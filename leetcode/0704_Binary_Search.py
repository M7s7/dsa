# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Typical binary search algorithm. 
    # Time Complexity: O(log N) - search space is halved every loop
    # Space Complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        # Less than/equals will catch the edge case of only one length arrays.
        while low <= high: 
            # We will use lower-middle as our middle
            mid = low + (high - low)//2
            val = nums[mid]
            
            if val == target:
                return mid
            
            elif val < target:
                low = mid + 1
                
            else:
                high = mid - 1
            
        # Exiting the loop means that the target does not exist in nums
        return -1
            
            