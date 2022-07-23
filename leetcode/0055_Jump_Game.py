# You are given an integer array nums. 
# You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Greedy approach. Go backwards through the array, shifting the goal.
    # Intuition: We can reach every index in an array with no zeroes. Thus, we can move our goals back until we reach a zero.
    # Then, we can check if there is an index to the left of zero that can jump over the gap.
# Time Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal_index = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal_index:
                goal_index = i
        
        if goal_index == 0:
            return True
        return False


# My initial implementation of our greedy approach. 
    # From the beginning, see the maximum leap we can make. If we can't jump over a zero, we lose.
    # Time and Space Complexity is the same as above
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        
        for i, num in enumerate(nums):
            max_index = max(max_index, i + num)
            if max_index >= len(nums) - 1:
                return True
            if num == 0 and max_index <= i:
                return False