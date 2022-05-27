# Given an integer x, return true if x is palindrome integer.
    # Follow up: Could you solve it without converting the integer to a string?

# Approach 1: String Conversion
    # Time complexity: O(N) from string conversion + loop// Space complexity; O(N) from list

def isPalindrome(self, x):
    x = str(x)
    
    # Set pointers
    left = 0
    right = len(x) - 1
    
    while left < right and len(x) > 1:
        if x[left] != x[right]:
            return False
        
        left += 1
        right -= 1
    
    return True