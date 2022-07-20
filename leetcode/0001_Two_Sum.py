# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# METHOD 1: OPTIMAL - ONE-PASS HASHMAP
# Create a hashmap (values:indices) and FILL IN ELEMENTS as you go. Iterating through the array, check if there is a matching number which would make TwoSum = target. If not, add the current number to the hashmap.
# This method allows us to avoid needed to check if we are using the same element twice (eg. if the array was 0, 1, 1, 2 it would make sure that we don't use the same one twice and instead we would use both indices 1 and 2)
# Time complexity: O(N) // Space complexity: O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store number:index
        values = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in values:
                return [i, values[complement]]
            values[num] = i
        
        return False