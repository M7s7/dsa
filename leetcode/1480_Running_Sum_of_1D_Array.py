# Given an array nums, return the running sum of nums.

# Approach - keep a running Sum.
    # Time Complexity: O(N) // Space Complexity: O(1) if not including output size
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        currSum = 0
        
        for value in nums:
            currSum += value
            sums.append(currSum)
        
        return sums