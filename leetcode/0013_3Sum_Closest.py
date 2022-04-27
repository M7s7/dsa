# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. 
# If there are more than one such triplet, return the sum of the triplet with the smallest sum.
# Time complexity is O(N^2) (+ nlogn for the sort) // Space complexity is O(N) for sorting. 
import math

def threeSumClosest(nums, target):
    # Sort array for 2 pointer
    nums.sort()
    # Initiate variables - diff records difference between target and 3Sum, result is the 3Sum with the lowest diff
    diff, result = math.inf, 0
    
    # Iterate through the array, creating subarrays on the right. Leave 2 spaces on the right for left/right pointers
    for index in range(len(nums) - 2):
        # Initiate the pointers
        left = index + 1
        right = len(nums) - 1
        
        # Do two-sum on the left subarray
        while left < right:
        # Track the lowest score for every move of the pointers
            threeSum = nums[left] + nums[right] + nums[index]
            if abs(threeSum - target) < diff:
                result = threeSum
                diff = abs(threeSum - target)
            
            # Conditionals to shift pointers, converging to the right value
            if threeSum == target:
                return threeSum
            elif threeSum < target:
                left += 1
            else:
                right -= 1
    
    return result