# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
# Return the single element that appears only once.


# Binary Search.
    # Intuition is that every number is PAIRED besides the target number. Thus, before the target number appears, we know that each ODD index should be different to the next number, and each INDEX number should be the same as the next.
    # However, once the single number is introduced, the opposite is true.
        # Time Complexity: O(log N) binary search
        # Space Complexity: O(1)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        # Loop exits when low and high are on the same index - we will converge on the target number. 
        while low < high:
            mid = low + (high - low)//2
            
        # These two conditions mean that the target number is either AT mid or to the left of mid. Thus, we do not want to exclude mid. 
            # Even indices
            if mid % 2 == 0 and nums[mid] != nums[mid + 1]:
                high = mid
            # Odd indices
            elif mid % 2 == 1 and nums[mid] == nums[mid + 1]:
                high = mid
        
        # This condition means that the target is to the RIGHT of mid. Since we know mid is not the target, we can remove it from our search space. 
            else: 
                low = mid + 1
            
        return nums[low]
    
    