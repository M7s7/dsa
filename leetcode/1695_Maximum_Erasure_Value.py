# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.
# Return the maximum score you can get by erasing exactly one subarray.


# Sliding window, keeping maximum sum of unique characters.
# Approach 1: Hashmap storing frequency
    # Time Complexity: O(N) - maximum two passes (i and start)
    # Space Complexity: O(N), storing each number as keys
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_sum, curr_sum = 0, 0
        freq = {}
        start = 0
        
        for i, val in enumerate(nums):
            curr_sum += val
            
            while val in freq:
                left_num = nums[start]
                curr_sum -= left_num
                freq[left_num] -= 1
                if freq[left_num] == 0:
                    del freq[left_num]
                start += 1
            
            freq[val] = 1
            max_sum = max(curr_sum, max_sum)

        return max_sum


# Approach 2: Hashmap storing location 
    # Complexity is identical as above
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_sum, curr_sum = 0, 0
        location = {}
        start = 0
        
        for i, val in enumerate(nums):
            curr_sum += val
            
            if val in location:
                target_i = location[val]
            
                while start <= target_i: 
                    left_num = nums[start]
                    curr_sum -= left_num
                    del location[left_num]
                    start += 1
            
            location[val] = i
            max_sum = max(max_sum, curr_sum)

        return max_sum