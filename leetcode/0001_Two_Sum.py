# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# METHOD 1: OPTIMAL - ONE-PASS HASHMAP
# Create a hashmap (values:indices) and FILL IN ELEMENTS as you go. Iterating through the array, check if there is a matching number which would make TwoSum = target. If not, add the current number to the hashmap.
# This method allows us to avoid needed to check if we are using the same element twice (eg. if the array was 0, 1, 1, 2 it would make sure that we don't use the same one twice and instead we would use both indices 1 and 2)
# Time complexity: O(N) // Space complexity: O(N)

def twoSum(self, nums, target):
    # Create hashmap
    indices = {}
    
    # Iterate through the array
    for index, value in enumerate(nums):
        # We want to find the other number that adds with our iterating number to get target
        number = target - value
        
        if number in indices:
            return index, indices[number]
        # If the number is not in the hashmap, store the current number in the hashmap and go to the next iteration
        else: 
            indices[value] = index    
    return

# Other two methods: BRUTE FORCE and TWO-PASS HASHMAP where we store the locations at the start and then check if we use the same element during the iteration
# Brute force: Time complexity: O(N^2), Space complexity: O(1)
# 2 Pass Hash: Time: O(N (actually 2N)) // Space complexity: O(N)