# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

# Bitwise operations - XOR to find A^B. Since the two numbers are distinct, A^B will be non-zero (thus, there will be at least one set bit). We can use this setbit to partition the array and XOR it again. 
    # Time Complexity: O(N) - unsure how long the bitshifting would take 
    # Space Complexity: O(1) 
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Find A XOR B
        two_xor = 0
        for num in nums:
            two_xor ^= num
        
        # Find a set bit - this bit will be different between the two target numbers
        set_bit = 1
        while two_xor & set_bit == 0:
            set_bit = set_bit << 1 # Same thing as saying set_bit * 2
        
        # Use the set bit to partition the array and get one target number
        target1 = 0
        for num in nums:
            if set_bit & num == 0:
                target1 ^= num
        
        target2 = two_xor ^ target1
        
        return target1, target2
                
        
        