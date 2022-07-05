# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.


# Approach 1: Find the set of UNIQUE numbers. 
    # Go through each unique number. If the number is the start of the sequence (aka no number that is -1 exists), start counting.
    # Note that checking only start sequences make this approach O(N) and not O(N^2).
        # Time Complexity: O(N) - O(N) to create unique set/hashmap, O(N) to go through numbers
        # Space Complexity: O(N)

    # Hashmap solution - use a hashmap to find unique numbers
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = {}
        max_length = 0
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        for num in freq:
            curr_length = 0
            # Skip non-start sequence numbers. 
            if num - 1 in freq:
                continue            
            # If we have the start of a sequence, check how high we can go
            while num + curr_length in freq:
                curr_length += 1
            max_length = max(curr_length, max_length)
        
        return max_length

    # Set solution - use set to find unique numbers
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_length = 0
        
        for num in nums:
            curr_length = 0
            if num - 1 in numSet:
                continue
            while num + curr_length in numSet:
                curr_length += 1
            
            max_length = max(max_length, curr_length)
        return max_length


# Sort solution. This is more complex and worse. Sort, then start counting sequences (skip duplicate numbers)
    # Time Complexity: O(nlogn) for sorting
    # Space Complexity: O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        max_length = 1
        curr_length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                curr_length += 1          
            else:
                curr_length = 1
            max_length = max(curr_length, max_length)
        
        return max_length