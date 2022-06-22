# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.


# Approach: Binary Search. We know that the minimum digit is at the 'pivot point', where the array is no longer in monotonic order.
    # Thus, we have to check which side is NOT in sorted order, and keep it. 
        # Time Complexity: O(log N)
        # Space Complexity: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        # Since we are finding a bound instead of a target number, it is a lot more convenient to use this variation
        while low < high:
            mid = low + (high - low)//2
            # Right side is unsorted
            if nums[mid] > nums[high]:
                low = mid + 1   
            # Left side is unsorted. Since mid is not checked in this condition, we keep it.        
            else: 
                high = mid
        
        return nums[low]

    # Edgecase
    # [4,5,6,7,0,1,2]. We see this edgecase again.
        # If we take the approach to DISCARD SORTED ARRAYS (line 14 as nums[mid] > nums[low] instead of what it is) instead of KEEPING UNSORTED ARRAYS, we will get the wrong answer.
        # The array will resolve to [0,1,2], then [1,2] then [2]. So this can easily find errors.