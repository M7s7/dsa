# You are given a 0-indexed integer array nums and a target element target.
# A target index is an index i such that nums[i] == target.
# Return a list of the target indices of nums after sorting nums in non-decreasing order. If no target, return an empty list.


# One pass - count the amount of numbers less than the target, and the amount of instances of the number.  
    # Time Complexity: O(N)
    # Space Complexity: O(1)
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less, number = 0, 0
        output = []
        
        # One pass through the array. Count the frequency of the target and the numbers less than the number. 
        for value in nums:
            if value == target:
                number += 1
                
            elif value < target:
                less += 1
        
        # Find the indices of the numbers
        for i in range(number):
            output.append(less)
            less += 1
        
        return output

# Sorting + pass through array
    # Time Complexity: O(n log n) for sorting
    # Space Complexity: O(N) for sorting
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        indices = []
        
        for i, value in enumerate(nums):
            if value == target:
                indices.append(i)
            
            elif value > target:
                return indices
        
        return indices

# Sorting + binary search for lower and upper bounds of the array (first instance of number and last instance of number)
    # Time Complexity: O(n log n) for sorting
    # Space Complexity: O(N) for sorting
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        indices = []
        
        lower_bound = self.findBounds(nums, target, True)
        upper_bound = self.findBounds(nums, target, False)
        
        if lower_bound != -1:
            for i in range(lower_bound, upper_bound + 1):
                indices.append(i)
    
        return indices 
    
    def findBounds(self, nums, target, lower: bool):
        low, high = 0, len(nums) - 1
        bound = -1
        
        while low <= high:
            mid = low + (high - low)//2
            val = nums[mid]
            
            if val > target:
                high = mid - 1
            
            elif val < target: 
                low = mid + 1
            
            if val == target:
                bound = mid
                
                if lower:
                    high = mid - 1
                
                else: 
                    low = mid + 1
        
        return bound
