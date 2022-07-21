# You are a professional robber planning to rob houses along a street. 
# Adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


# APPROACH:
    # Find the maximum profit we can get from each house. With our base cases (0 and 1 indexed house), we can calculate every subsequent houses max path.
    # We can either rob the path going through the previous house, or rob our current house (which will be part of the i - 2 house path)
# Recursive
    # Time Complexity: Very high
    # Space Complexity: O(N) I think?
class Solution:    
    def rob(self, nums: List[int]) -> int:    
        def max_profit_path(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            return max(max_profit_path(i - 1), max_profit_path(i - 2) + nums[i])
        return max_profit_path(len(nums) - 1)


# Top Down DP
    # Time Complexity: O(N)
    # Space Complexity: O(N)
class Solution:    
    def rob(self, nums: List[int]) -> int: 
        if len(nums) == 1:
            return nums[0]
        memo = {
            0 : nums[0],
            1 : max(nums[0], nums[1])
        }

        def max_profit_path(i):
            if i in memo:
                return memo[i]
            profit = max(max_profit_path(i - 1), max_profit_path(i - 2) + nums[i])
            memo[i] = profit
            return memo[i]
        return max_profit_path(len(nums) - 1)


# Bottom Up DP w/ memoization
    # Time Complexity: O(N)
    # Space Complexity: O(N)
class Solution:    
    def rob(self, nums: List[int]) -> int: 
        memo = {}
        
        max_profit = 0
        for i in range(len(nums)):
            if i == 0:
                memo[i] = nums[i]
            elif i == 1:
                memo[i] = max(nums[i], nums[i - 1])
            else:
                max_profit = max(memo[i - 1], nums[i] + memo[i - 2])
                memo[i] = max_profit
        
        return memo[i]


# Bottom UP DP w/ constant variables
    # Time Complexity: O(N)
    # Space Complexity: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        far, close = 0, 0
        for i in range(len(nums)):
            max_profit = max(close, far + nums[i])
            far = close
            close = max_profit
        
        return max_profit