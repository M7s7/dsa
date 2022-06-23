# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Approach 1: Bitwise Operation: XOR
    # Time Complexity: O(N)
    # Space Complexity: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numxor = 0
        for num in nums:
            numxor ^= num
        return numxor


# Approach 2: Set
    # Time Complexity: O(N), 3N
    # Space Complexity: O(N) or N/2
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        actualSum = 0
        for num in nums:
            actualSum += num  
            
        nums = set(nums)
        doubleSum = 0
        for num in nums:
            doubleSum += num   
        doubleSum *= 2 

        return doubleSum - actualSum


# Approach 3: Frequency hashmap
    # Time Complexity: O(N)
    # Space Complexity: O(N)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        for key, frequency in freq.items():
            if frequency == 1:
                return key
        