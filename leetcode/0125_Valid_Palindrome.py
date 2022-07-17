# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.


# Typical two-pointers solution.
    # Time Complexity: O(N)
    # Space Complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left <= right:
            if s[left].isalnum() == False:
                left += 1
                continue
            if s[right].isalnum() == False:
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True