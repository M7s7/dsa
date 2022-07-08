# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
    # Open brackets must be closed by the same type of brackets.
    # Open brackets must be closed in the correct order.


# Approach: Stack and hashmap.
    # Time Complexity: O(N)
    # Space Complexity: O(N)
import collections
class Solution:
    def isValid(self, s: str) -> bool:
        # Stack keeps track of latest opening bracket
        stack = collections.deque()
        # Hashmap - mapping closing brackets to what opening bracket they match with
        brackets = {
            ')':'(',
            ']':'[',
            '}':'{'
        }     
        
        for char in s:
            # If closing brackets, check top element
            if char in brackets:
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else:
                    return False
            # Always push opening brackets
            else:
                stack.append(char)
        
        if not stack:
            return True
        return False