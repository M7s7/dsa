# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
# Given an integer n, return its complement.

# Bitwise. Two different implentations of bitwise ops. Both implementations have to be careful of leading 0s.  
# Time Complexity: O(bits) - number of bits in the number
# Space Complexity: O(1)

# Approach 1: XOR the number with all ones (in binary)
    # To find this number, we will keep adding ones until we have a bigger number, to avoid XORing leading 0s. 
    # Example: [1111] for [1001], but [111] for [0110]. We don't want to XOR 1 with a leading 0. 
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        all_ones = 1
        
        while all_ones < n: 
            all_ones = all_ones << 1 | 1 # same as "all_ones * 2 + 1"
    
        return n ^ all_ones

# Approach 2: XOR each individual bit with a left shifting set bit. 
    # To avoid XORing leading 0s, stop XORing when the shifting bit is smaller/equal to the number.
    # Time Complexity: O(bits)
    # Space Complexity: O(1)
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Edge case
        if n == 0:
            return 1
        
        # XOR each individual bit
        swap_bit = 1
        while swap_bit <= n:
            n ^= swap_bit
            swap_bit <<= 1
    
        return n