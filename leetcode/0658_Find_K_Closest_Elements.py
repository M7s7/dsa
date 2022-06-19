# Given a sorted integer array arr, two integers k and target (x), return the k closest integers to target in the array. The result should also be sorted in ascending order.
# An integer a is closer to x than an integer b if:
#    |a - x| < |b - x|, or
#    |a - x| == |b - x| and a < b (tiebreaker - if equally distant, the smaller number is closer)


# Binary Search to find closest number, then two pointers to expand closest numbers
    # Time Complexity: O(logN + k) - logN to find the closest number, then k to expand the sub-array
    # Space Complexity: O(1)
class Solution:
    def findClosestElements(self, nums: List[int], k: int, target: int) -> List[int]:
        low, high = 0, len(nums) - 1
        # If the target is <= than the entire array, we can return the smallest k numbers
        if target <= nums[low]:
            return nums[:k]
        # If the target is >= than the entire array, we can return the largest k numbers
        elif target >= nums[high]:
            return nums[-k:]
        
        # Find first largest number than target. We can guarantee that the closest number is not indexed 0 or len(nums) - 1 because of the early returns above
        while low < high:
            mid = low + (high - low)//2
            value = nums[mid]
            if value < target:
                low = mid + 1    
            else:
                high = mid
        
        # Now that we have the first smallest and first largest number, we can determine which is the closest number
        if abs(nums[low - 1] - target) <= abs(nums[low] - target):
            start = end = low - 1
        else:
            start = end = low
        
        # Since we already have the closest number, we only need to find k - 1 other numbers. Our goal is to find the start index - smallest closest k element
        i = 1
        while i < k:
            # If our low bound is at the end before we find k elements, we can return smallest k
            if start == 0:
                break
            # We can expand the low bound if: 1) our high bound is at the end, or the low bound is closer than the high bound
            elif end == len(nums) - 1 or abs(nums[start - 1] - target) <= abs(nums[end + 1] - target):
                start -= 1
            # Else, expand the high bound
            else:
                end += 1    
            i += 1
        
        return nums[start:start+k]