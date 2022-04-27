# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. 
# If there are more than one such triplet, return the sum of the triplet with the smallest sum.
# Time complexity is O(N^2) (+ nlogn for the sort) // Space complexity is O(N) for sorting. 

import math

def main():
    arr = [-3, -1, 1, 2]
    target = 1
    print(threeSum_close(arr, target))


def threeSum_close(nums, target):
    # Sort the array
    nums.sort()
    # Initiate variables
    diff, result = math.inf, math.inf

    # Loop over the array and create a two-sum problem on the right of the index. Again, index does not need to go over the whole array because 2 spots are needed to the right. 
    for index in range(len(nums) - 2):
        # Initiate our pointers
        left = index + 1
        right = len(nums) - 1

        # For the subarray on the right, perform two-sum. Our tracking condition will be if diff is getting smaller. 
        while left < right: 
            # Calculate sum of triplet. Check if it is the current closest; if so, store value
            threeSum = nums[index] + nums[left] + nums[right]
            if abs(threeSum - target) < diff:
                # Checking if the current sum is smaller than stored sum. If so, record that result instead
                result = threeSum
                # New diff as benchmark
                diff = abs(threeSum - target)
            # Returns the smallest number if difference is the same
            elif abs(threeSum - target) == diff:
                result = min(threeSum, result)
            # If the difference is zero, we have a solution 
            if threeSum == target:
                return target
            
            # If the difference between threeSum and target is positive, we need to decrement right to lower value
            elif threeSum - target > 0: 
                right -= 1     
            else:
                left += 1
    return result


main()
