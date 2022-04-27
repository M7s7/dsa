# COMPLETED ON LINTCODE
# Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
# This question is similar to ThreeSum target, but the trick is with the counter. Every time a solution is found, we can add all triplets of (nums[i], nums[left], nums[left + 1 to right]) because the array is sorted. 
# Time complexity is O(N^2) (+ nlogn for sorting) // Space complexity is O(N) for sorting. 

def three_sum_smaller(self, nums: List[int], target: int) -> int:
    # Sort numbers for two-pointer
    nums.sort()
    # Initiate triplet counter
    count = 0

    # Initiate index variable that increments over the window; leave 2 spaces for left/right pointers
    for i in range(len(nums) - 2):
        # Initiate left and right pointers
        left = i + 1
        right = len(nums) - 1

        # Create TwoSum loop:
        while left < right:
            threeSum = nums[i] + nums[right] + nums[left]
            # Condition is met - implicitly, all numbers to the left of the right pointer are also valid as they only go smaller, so count them too
            if threeSum < target:
                count += right - left
                # Increment left pointer higher and recheck the condition
                left += 1
            
            # If condition is not met, we need to lower threeSum
            else: right -= 1
    return count