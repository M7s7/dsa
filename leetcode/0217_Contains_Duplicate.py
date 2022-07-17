# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Hashmap solution. Slightly better than set solution as it can terminate early
    # Time Complexity: O(N)
    # Space Complexity: O(N)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appears = {}
        for num in nums:
            if num in appears:
                return True
            appears[num] = True   
        return False

# Set solution
    # Time Complexity: O(N)
    # Space Complexity: O(N)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len_set = len(set(nums))
        if len_set == len(nums):
            return False
        return True